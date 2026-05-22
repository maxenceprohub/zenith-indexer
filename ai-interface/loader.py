import os
from pathlib import Path

def scanner_documents():
    """
    Localise tous les fichiers .txt dans le dossier spécifié.
    Calcule le chemin par rapport au dossier parent du script.
    """
    chemin_base = Path(__file__).parent / "documents"
    
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
    """Calcule le total de mots et la densité."""
    mots = contenu_texte.split()
    total_mots = len(mots)
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
        print(f"Rapport généré : '{nom_rapport}'")
        print(f"\n[INFO] Rapport sauvegarde avec succes sous : {chemin_rapport.resolve()}")

    except Exception as e:
        print(f"\n[ERREUR] Impossible de sauvegarder le rapport : {e}")
if __name__ == "__main__":
    
    fichiers = scanner_documents()

    print("--- ZENITH INDEXER | ANALYSEUR DE DOCUMENTS ---")

    if not fichiers:
        chemin_attendu = Path(__file__).parent.parent / "documents"
        print(f"Erreur : Aucun fichier trouvé dans 'documents'.")
        print(f"dépose tes fichiers .txt directement dans : '{chemin_attendu}'")
    else:
        print(f"\nTrouvé {len(fichiers)} fichier(s) :")
        for index, chemin in enumerate(fichiers):
            print(f"[{index}] {chemin.name}")
        
        try:
            selection = int(input("\nSélectionnez l'index d'un fichier à analyser : "))
            
            if 0 <= selection < len(fichiers):
                fichier_selectionne = fichiers[selection]
                contenu = lire_contenu_fichier(fichier_selectionne)
                
                if contenu.startswith("[ERREUR"):
                    print(f"\n{contenu}")
                    print("Analyse annulé.")
                else:
                
                    requete_recherche = input(f"Entrez le mot-clé à chercher dans '{fichier_selectionne.name}' : ")
                    occurrences = obtenir_frequence_mot_cle(contenu, requete_recherche)
                
                    # On calcule les métriques ici
                    total, pourcent = calculer_metriques(contenu, occurrences)

                if occurrences > 0:
                    print(f"\n--- RÉSULTATS DE L'ANALYSE ---")
                    print(f"Nombre total de mots dans le document : {total}")
                    print(f"Le mot '{requete_recherche}' apparaît {occurrences} fois.")
                    print(f"Densité du mot-clé : {pourcent}%")
                else:
                    print(f"\nAucune correspondance : Le mot '{requete_recherche}' n'a pas été trouvé.")
                    print(f"Note : Le document contient tout de même {total} mots.")

                sauvegarder_rapport(fichier_selectionne.name, requete_recherche, occurrences, total, pourcent)

            else:
                print("Erreur : Index invalide.")

        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide.")

    print("\n--- SESSION TERMINÉE ---")