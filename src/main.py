import os
from dotenv import load_dotenv
import logging
from pathlib import Path

# On importe les 3 classes depuis notre fichier analyzer.py
from analyzer import DocumentManager, TextAnalyzer, ZenithAI

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("zenith.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

load_dotenv()

if __name__ == "__main__":
    
    # On instancie nos managers globaux au démarrage
    manager_doc = DocumentManager()
    zenith_ia = ZenithAI()

    fichiers = manager_doc.scanner_documents()

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
                contenu = manager_doc.lire_contenu_fichier(fichier_selectionne)
                
                if contenu.startswith("[ERREUR"):
                    logging.error(f"\n{contenu}")
                    logging.info("Analyse annulé.")
                else:
                    # On injecte le texte lu dans notre analyseur dédié
                    analyseur = TextAnalyzer(contenu)
                
                    requete_recherche = input(f"Entrez le mot-clé à chercher dans '{fichier_selectionne.name}' : ")
                    occurrences = analyseur.obtenir_frequence_mot_cle(requete_recherche)
                
                    total, pourcent = analyseur.calculer_metriques(occurrences)

                if occurrences > 0:
                    logging.info(f"\n--- RÉSULTATS DE L'ANALYSE ---")
                    logging.info(f"Nombre total de mots dans le document : {total}")
                    logging.info(f"Le mot '{requete_recherche}' apparaît {occurrences} fois.")
                    logging.info(f"Densité du mot-clé : {pourcent}%")
                else:
                    logging.info(f"\nAucune correspondance : Le mot '{requete_recherche}' n'a pas été trouvé.")
                    logging.info(f"Note : Le document contient tout de même {total} mots.")

                manager_doc.sauvegarder_rapport(fichier_selectionne.name, requete_recherche, occurrences, total, pourcent)
                
                mode_ia = input("\nVoulez-vous interroger l'IA sur ce document ? (o/n) : ")
                if mode_ia.lower() == 'o':
                    logging.info("Mode Discussion Activé (tapez 'quitter' pour s'arrêter)")

                    while True:
                        question_ia = input("Entrez votre questions pour l'IA : ")
                        if question_ia.lower() == "quitter":
                            logging.info("Fin de la session AI.")
                            break

                        logging.info("Réfléxion En Cours...")
                        reponse_ia = zenith_ia.interogger_ia_sur_document(contenu, question_ia)
                        print(f"\n--- RÉPONSE DE L'IA ---\n{reponse_ia}")
            else:
                logging.error("Erreur : Index invalide.")

        except ValueError:
            logging.error("Erreur : Veuillez entrer un nombre valide.")

    logging.info("\n--- SESSION TERMINÉE ---")