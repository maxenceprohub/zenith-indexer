
import os
from openai import OpenAI
from pathlib import Path
from dotenv import load_dotenv
import logging
import re

logging.basicConfig(
    level=logging.INFO, # On enregistre tout ce qui est INFO, WARNING et ERROR
    format="%(asctime)s - [%(levelname)s] - %(message)s", # Structure de la ligne : Heure - [Niveau] - Message
    datefmt="%Y-%m-%d %H:%M:%S", # Format de l'heure : Année-Mois-Jour Heure:Minute:Seconde
    handlers=[
        logging.FileHandler("zenith.log", encoding="utf-8"), # Écrit automatiquement dans un fichier 'zenith.log'
        logging.StreamHandler() # Continue d'afficher les messages dans ton terminal de commande
    ]
)

load_dotenv()

def interogger_ia_sur_document(contenu_texte, question):

    if not os.getenv("OPENAI_API_KEY"):
        return "[ERREUR] : Clé API OpenAI non trouvée. Veuillez définir OPENAI_API_KEY dans votre environnement (.env)."
    
    try:

        client = OpenAI()

        system_prompt = ("Tu es Zenith IA, l'assistant intelligent du Zenith Indexer.\n"
            "Voici le contenu d'un document texte local. Réponds à la question de l'utilisateur "
            "en te basant UNIQUEMENT sur ce texte. Si la réponse n'est pas dans le texte, dis-le poliment.\n\n"
            f"--- DEBUT DU DOCUMENT ---\n{contenu_texte}\n--- FIN DU DOCUMENT ---")
        
        reponse = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question}
            ], 
            temperature=0.3
        )

        return reponse.choices[0].message.content
    
    except Exception as e:
        return f"[ERREUR IA] Impossible d'obtenir une réponse : {e}"


def scanner_documents():
    """
    Localise tous les fichiers .txt dans le dossier spécifié.
    Calcule le chemin par rapport au dossier parent du script.
    """
    chemin_base = Path(__file__).parent.parent / "documents"
    
    if not chemin_base.exists():
        chemin_base.mkdir(parents=True, exist_ok=True)
        return []
    
    return list(chemin_base.glob('*.txt'))

def lire_contenu_fichier(chemin_fichier):
    """Lit et renvoie le contenu textuel d'un fichier donné."""
    try:
        with open(chemin_fichier, 'r', encoding='utf-8') as f:
            return f.read()
        
    except UnicodeDecodeError:
        return f"[ERREUR_FORMAT] Le fichier n'est pas un fichier texte UTF-8 valide."
        
    except PermissionError:
        return f"[ERREUR_PERMISSION] : Accès refusé au fichier '{chemin_fichier}'"

    except Exception as e: 
        return f"[ERREUR_INCONNUE] : {e}"    

def obtenir_frequence_mot_cle(contenu_texte, mot_cle):
    """Calcule le nombre d'occurrences d'un mot-clé dans le texte."""
    contenu_normalise = contenu_texte.lower()
    mot_cle_normalise = mot_cle.lower()    
    return contenu_normalise.count(mot_cle_normalise)

def calculer_metriques(contenu_texte, nombre_occurences):

    texte_nettoye = re.sub(r"[^\w\s]", " ", contenu_texte)

    mots_bruts = texte_nettoye.lower().split()

    stopword = ["le", "la", "les", "de", "des", "un", "une", "et", "en", "que", "pour"]

    mots_filtres =[]
    for mot in mots_bruts:
        if mot not in stopword:
            mots_filtres.append(mot)

    """Calcule le total de mots et la densité.""" 
    total_mots = len(mots_filtres)
    densite = (nombre_occurences / total_mots) * 100 if total_mots > 0 else 0
    return total_mots, round(densite, 2)

def sauvegarder_rapport(nom_fichier_analyse, mot_cle, occurences, total_mots, densite):
    """Génère un fichier texte contenant les résultats de l'analyse."""
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

if __name__ == "__main__":
    
    fichiers = scanner_documents()

    print("--- ZENITH INDEXER | ANALYSEUR DE DOCUMENTS ---")

    if not fichiers:
        chemin_attendu = Path(__file__).parent.parent / "documents"
        logging.error(f"Erreur : Aucun fichier trouvé dans 'documents'.")
        logging.info(f"dépose tes fichiers .txt directement dans : '{chemin_attendu}'")
    else:
        logging.info(f"\nTrouvé {len(fichiers)} fichier(s) :")
        for index, chemin in enumerate(fichiers):
            logging.info(f"[{index}] {chemin.name}")
        
        try:
            selection = int(input("\nSélectionnez l'index d'un fichier à analyser : "))
            
            if 0 <= selection < len(fichiers):
                fichier_selectionne = fichiers[selection]
                contenu = lire_contenu_fichier(fichier_selectionne)
                
                if contenu.startswith("[ERREUR"):
                    logging.error(f"\n{contenu}")
                    logging.info("Analyse annulé.")
                else:
                
                    requete_recherche = input(f"Entrez le mot-clé à chercher dans '{fichier_selectionne.name}' : ")
                    occurrences = obtenir_frequence_mot_cle(contenu, requete_recherche)
                
                    # On calcule les métriques ici
                    total, pourcent = calculer_metriques(contenu, occurrences)

                if occurrences > 0:
                    logging.info(f"\n--- RÉSULTATS DE L'ANALYSE ---")
                    logging.info(f"Nombre total de mots dans le document : {total}")
                    logging.info(f"Le mot '{requete_recherche}' apparaît {occurrences} fois.")
                    logging.info(f"Densité du mot-clé : {pourcent}%")
                else:
                    logging.info(f"\nAucune correspondance : Le mot '{requete_recherche}' n'a pas été trouvé.")
                    logging.info(f"Note : Le document contient tout de même {total} mots.")

                sauvegarder_rapport(fichier_selectionne.name, requete_recherche, occurrences, total, pourcent)
                
                mode_ia = input("\nVoulez-vous interroger l'IA sur ce document ? (o/n) : ")
                if mode_ia.lower() == 'o':
                    logging.info("Mode Discussion Activé (tapez 'quitter' pour s'arrêter)")

                    while True:

                        question_ia = input("Entrez votre questions pour l'IA :")
                        if question_ia.lower() == "quitter":
                            logging.info("Fin de la session AI.")
                            break

                        logging.info("Réfléxion En Cours...")
                        reponse_ia = interogger_ia_sur_document(contenu, question_ia)
                        print(f"\n--- RÉPONSE DE L'IA ---\n{reponse_ia}")
            else:
                logging.error("Erreur : Index invalide.")

        except ValueError:
            logging.error("Erreur : Veuillez entrer un nombre valide.")

    logging.info("\n--- SESSION TERMINÉE ---")