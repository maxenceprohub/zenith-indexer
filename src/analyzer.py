import os
from pathlib import Path
import logging
import re
import ollama

class DocumentManager:
    """Gère la localisation, la lecture et la sauvegarde des rapports."""
    def __init__(self):
        pass

    def scanner_documents(self):
        chemin_base = Path(__file__).parent.parent / "documents"
        if not chemin_base.exists():
            chemin_base.mkdir(parents=True, exist_ok=True)
            return []
        return list(chemin_base.glob('*.txt'))

    def lire_contenu_fichier(self, chemin_fichier):
        try:
            with open(chemin_fichier, 'r', encoding='utf-8') as f:
                return f.read()
        except UnicodeDecodeError:
            return f"[ERREUR_FORMAT] Le fichier n'est pas un fichier texte UTF-8 valide."
        except PermissionError:
            return f"[ERREUR_PERMISSION] : Accès refusé au fichier '{chemin_fichier}'"
        except Exception as e: 
            return f"[ERREUR_INCONNUE] : {e}"    

    def sauvegarder_rapport(self, nom_fichier_analyse, mot_cle, occurrences, total_mots, densite):
        nom_rapport = f"rapport_{nom_fichier_analyse}"
        chemin_rapport = Path(__file__).parent / nom_rapport
        try:
            with open(chemin_rapport, "w", encoding='utf-8') as f:
                f.write("==================================================\n")
                f.write("         ZENITH INDEXER - RAPPORT D'ANALYSE       \n")
                f.write("==================================================\n\n")
                f.write(f"Fichier analyse : {nom_fichier_analyse}\n")
                f.write(f"Mot-cle recherche : '{mot_cle}'\n\n")
                f.write(f"--- METRIQUES ---\n")
                f.write(f"Nombre total de mots : {total_mots}\n")
                f.write(f"Nombre d'occurrences : {occurrences}\n")
                f.write(f"Densite du mot-cle   : {densite}%\n\n")
                f.write("==================================================\n")
                f.write("Genere automatiquement par Zenith Indexer (Prototype Python)\n")
            logging.info(f"Rapport généré : '{nom_rapport}'")
            logging.info(f"\n[INFO] Rapport sauvegarde avec succes sous : {chemin_rapport.resolve()}")
        except Exception as e:
            logging.error(f"\n[ERREUR] Impossible de sauvegarder le rapport : {e}")


class TextAnalyzer:
    """Gère l'analyse du texte, la fréquence et le calcul des métriques."""
    def __init__(self, contenu_texte):
        self.contenu = contenu_texte

    def obtenir_frequence_mot_cle(self, mot_cle):
        contenu_normalise = self.contenu.lower()
        mot_cle_normalise = mot_cle.lower()    
        return contenu_normalise.count(mot_cle_normalise)

    def calculer_metriques(self, nombre_occurences):
        texte_nettoye = re.sub(r"[^\w\s]", " ", self.contenu)
        mots_bruts = texte_nettoye.lower().split()
        stopword = ["le", "la", "les", "de", "des", "un", "une", "et", "en", "que", "pour"]
        
        mots_filtres = []
        for mot in mots_bruts:
            if mot not in stopword:
                mots_filtres.append(mot)

        total_mots = len(mots_filtres)
        densite = (nombre_occurences / total_mots) * 100 if total_mots > 0 else 0
        return total_mots, round(densite, 2)
    
    def decouper_en_chuncks(self, taille_chunk=300, chevauchement=50):

        mot = self.contenu.split()
        chunks = []
        
        i = 0
        while i < len(mot):

            chunk = mot[i:i + taille_chunk]
            chunks.append(" ".join(chunk))
            i += taille_chunk - chevauchement

        return chunks


class ZenithAI:
    """Gère la connexion et les requêtes avec l'API OpenAI."""
    def __init__(self):
        self.modele = "llama3.2:1b"
        self.historique_discussion = []
        self.contexte_initialise = False

    def interrogger_ia_sur_document(self, contexte, question):
        try:
            if not self.contexte_initialise:
                prompt_systeme = (
                    "Tu es l'intelligence artificielle de Zenith Indexer.\n"
                    "Réponds à la question de l'utilisateur en français en t'appuyant uniquement sur les morceaux de texte fournis.\n"
                    "Si la réponse n'est pas dans le texte, dis poliment que tu ne sais pas.\n\n"
                    f"--- MORCEAUX DE TEXTE FOURNIS ---\n{contexte}"
                )

                self.historique_discussion.append({
                    "role": "system",
                    "content": prompt_systeme
                })

                self.contexte_initialise = True

            self.historique_discussion.append({
                "role": "user",
                "content": question
            })

            reponse = ollama.chat(
                model=self.modele,
                messages=self.historique_discussion
            )

            reponse_texte = reponse['message']['content']

            self.historique_discussion.append({
                "role": "assistant",
                "content": reponse_texte
            })

            return reponse_texte

        except Exception as e:
            return f"[ERREUR IA LOCALE] Impossible de joindre le modèle : {e}"