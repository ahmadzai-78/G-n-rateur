🧠 Générateur de texte local (Flask)
Ce projet est une application web simple en Python Flask qui permet de générer différents types de textes automatiquement sans utiliser d’API externe.

🚀 Fonctionnalités
Génération de descriptions de produits, titres accrocheurs et emails promotionnels à partir d'une idée.

Interface responsive avec Bootstrap.

Fonction copier-coller pour récupérer facilement le texte généré.

Tout est exécuté en local : aucune donnée n’est envoyée à un serveur externe.

🔧 Technologies utilisées
Python 3

Flask

HTML/CSS (Bootstrap 5)

Jinja2

▶️ Lancer le projet
Clone le dépôt :
git clone 
cd generateur-local
Installe les dépendances :

pip install -r requirements.txt
Lance l’application :


python app.py
Ouvre ton navigateur et rends-toi sur :
http://127.0.0.1:5000

📂 Structure du projet
generateur-local/
├── app.py               # Fichier principal Flask
├── requirements.txt     # Dépendances Python
├── templates/
│   └── index.html
