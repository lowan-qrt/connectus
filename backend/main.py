from flask import Flask, render_template, request
import datetime
"""
Render template :   Permet de passer des variables python au code html pour les afficher sur la page -> exemple avec heure.html et eleves.html
                    Permet aussi de lancer le fichier html depuis le code python. Tout est lancé depuis main.py

request :   Permet de récupérer des paramètres écrit dans l'URL : http://127.0.0.1:5000/eleves?c=2A&autre=blabla ici la fonction 
            request.arg.get('c') renverra 2A -> Voir exemple sur @app.route('/eleves')   
"""

app = Flask(__name__)

@app.route('/') #@app.route('/') permet de définir vers quel url va servir le code python. Ici seulement index.html
def bonjour():
    return render_template('index.html')

@app.route('/heure')
def heure():
    date_heure = datetime.datetime.now()
    h = date_heure.hour
    m = date_heure.minute
    s = date_heure.second
    return render_template('heure.html', heure=h, minute=m, seconde=s) #comme dit précédemment, on passe des variable python à notre dossier html

liste_eleves =  [
    {'nom': 'Pomier', 'prenom': 'Max', 'classe': 'TA'},
    {'nom': 'Quarton', 'prenom': 'Lowan', 'classe': 'TB'},
    {'nom': 'Onillon', 'prenom': 'Jean', 'classe': 'TC'},
    {'nom': 'Vigneron', 'prenom': 'Martin', 'classe': 'TD'},
]

@app.route('/eleves')
def eleves():
    classe = request.args.get('c') 
    if classe:
        eleves_selectionnes = [eleve for eleve in liste_eleves if eleve['classe'] == classe] #permet d'afficher seulement les élèves ayant un paramètre concordant avec le paramètre de l'URL qu'on a récupéré
    else:
        eleves_selectionnes = [] #permet de renvoyer un tableau vide s'il n'y a pas d'lélèves correspondant à la recherche 
    return render_template('eleves.html', eleves=eleves_selectionnes) 

if __name__ == '__main__': #permet de run l'appli
    app.run(debug=True)