# Gestionnaire de Scripts Python

## Description

Ce projet est un service web Python permettant de planifier et d'exécuter des scripts Python de manière périodique. Il offre une interface utilisateur simple pour gérer les scripts, leurs planifications, et visualiser les logs d'exécution.

## Fonctionnalités

- Ajout de scripts Python avec planification personnalisée (utilisant la syntaxe cron)
- Suppression de scripts planifiés
- Visualisation de la liste des scripts planifiés
- Affichage des logs d'exécution
- Interface web pour la gestion des scripts et la visualisation des logs

## Prérequis

- Python 3.7+
- pip (gestionnaire de paquets Python)

## Installation

1. Clonez ce dépôt :
git clone https://github.com/votre-nom/gestionnaire-scripts-python.git
cd gestionnaire-scripts-python
Copy
2. Installez les dépendances :
pip install -r requirements.txt
Copy
3. Activez l'environnement :
venv/Scripts/Activate
Copy
source bin/activate
Copy
4. Initialisez la base de données :
python init_db.py


Copy
## Structure du projet
project/
│
├── app.py            # Application Flask principale
├── scheduler.py      # Gestionnaire de planification des tâches
├── database.py       # Configuration de la base de données
├── models.py         # Modèles de données
├── templates/
│   └── index.html    # Interface utilisateur web
└── scripts/
└── (vos scripts Python à exécuter)
Copy
## Utilisation

1. Démarrez l'application :
python app.py
Copy
2. Ouvrez un navigateur et accédez à `http://localhost:5000`

3. Utilisez l'interface web pour :
- Ajouter de nouveaux scripts en spécifiant leur nom, chemin, et planification
- Visualiser la liste des scripts planifiés
- Supprimer des scripts existants
- Consulter les logs d'exécution

## Planification des scripts

La planification utilise la syntaxe cron. Voici quelques exemples :

- `* * * * *` : Toutes les minutes
- `0 * * * *` : Toutes les heures
- `0 0 * * *` : Tous les jours à minuit
- `0 0 * * 0` : Tous les dimanches à minuit
- `0 0 1 * *` : Le premier jour de chaque mois

## Développement

Pour étendre les fonctionnalités de cette application :

1. Ajoutez de nouvelles routes dans `app.py`
2. Modifiez les modèles dans `models.py` si nécessaire
3. Mettez à jour l'interface utilisateur dans `templates/index.html`

## Sécurité

Attention : Cette application est conçue pour un usage local ou dans un environnement de confiance. N'exposez pas ce service directement sur Internet sans ajouter des mesures de sécurité appropriées (authentification, HTTPS, etc.).

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## Licence

[MIT License](https://opensource.org/licenses/MIT)