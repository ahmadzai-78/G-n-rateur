from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "devmonde_secret"

def generer_description(idee):
    templates = [
        "Découvrez notre {idee}, alliant style, légèreté et praticité au quotidien.",
        "Le {idee} idéal : léger, robuste et parfaitement adapté à vos besoins.",
        "Optez pour un {idee} qui vous accompagne partout avec confort et efficacité.",
        "Conçu pour les esprits actifs, ce {idee} offre un équilibre parfait entre design et performance.",
        "Transformez votre quotidien avec ce {idee}, pensé pour allier élégance et fonctionnalité."
    ]
    return random.choice(templates).format(idee=idee)

def generer_titre(idee):
    return f"{idee.capitalize()} : la nouvelle tendance à ne pas manquer !"

def generer_email(idee):
    return f"""Bonjour,

Vous cherchez un produit pratique et stylé ?
Découvrez notre {idee}, conçu pour vous simplifier la vie.

Essayez-le dès aujourd’hui !

À très bientôt."""

@app.route("/", methods=["GET", "POST"])
def index():
    resultat = None
    if "historique" not in session:
        session["historique"] = []

    if request.method == "POST":
        idee = request.form.get("idee")
        mode = request.form.get("mode")

        if idee:
            if mode == "description":
                resultat = generer_description(idee)
            elif mode == "titre":
                resultat = generer_titre(idee)
            elif mode == "email":
                resultat = generer_email(idee)

            session["historique"].append(resultat)

    return render_template("index.html", result=resultat, historique=session["historique"])

if __name__ == "__main__":
    print("✅ Le serveur Flask démarre sur http://localhost:5000")
    app.run(debug=True)
