#coding:utf-8
from flask import Flask, render_template, request
import sql_bdd

# Application
app = Flask(__name__)

# //////// Pages ////////
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/connexion')
def connection():
    return render_template('connection.html')

@app.route('/inscription')
def inscription():
    return render_template('inscription.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/plus-d-infos')
def more_infos():
    return render_template('more_infos.html')
# ///////////////////////

@app.route('/ma-page', methods=['POST'])
def sign_in():
    args = request.form # get form elements
    print('\n\tMESSAGE: Datas sent by form:')
    for arg, value in args.items():
        print(f'{arg} : {value}')
    print('\n')
    pseudo = args.get('pseudo')
    password = args.get('password')
    email = args.get('email')
    firstname = args.get('first_name')
    lastname = args.get('last_name')
    birthday = args.get('birthday')
    phone = args.get('phone')
    answer = sql_bdd.signIn(pseudo, password, email, firstname, lastname, birthday, phone) # sent elements to db
    
    if answer == False:
        errorPseudo = "Oups ! Ce nom d'utilisateur est déjà utilisé. Essayez-en un autre."
        render_template('inscription.html', errorPseudo = errorPseudo)
    else:
        return render_template('userpage.html', fname=firstname, lname=lastname)

# Execute the app
if __name__ == '__main__':
    app.run(debug=True)