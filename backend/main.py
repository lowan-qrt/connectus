# Coding: utf-8
from flask import Flask, render_template, request
import sql_bdd

# Application
app = Flask(__name__)

# //////////// Pages /////////////
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/connexion', methods=['POST', 'GET'])
def connection():
    return render_template('connection.html')

@app.route('/inscription')
def inscription():
    return render_template('inscription.html', condition=True)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/plus-d-infos')
def more_infos():
    return render_template('more_infos.html')

@app.route('/fil_d_actualite/<fname>/<lname>/<pseudo>')
def userpage(fname, lname, pseudo):
    return render_template('userpage.html', fname=fname, lname=lname, pseudo=pseudo)

@app.route('/Bienvenue', methods=['POST'])
def sign_in():
    datas = request.form # get elements from form

    print('\n\t>>> MESSAGE: [Datas received by form 1]\n') # console message
    for arg, value in datas.items():
        print(f'\t{arg}: {value}')

    pseudo = datas.get('pseudo')
    password = datas.get('password')
    email = datas.get('email')
    firstname = datas.get('first_name')
    lastname = datas.get('last_name')
    birthday = datas.get('birthday')
    phone = datas.get('phone')

    condition = sql_bdd.signIn(pseudo, password, email, firstname, lastname, birthday, phone) # check the unicity

    if not condition:
        # Redirection
        print(condition)
        return render_template('inscription.html', condition=condition)
    else:
        # Welcome
        return render_template('userpage.html', fname=firstname, lname=lastname)

@app.route("/Fil des posts", methods=['POST'])
def log_in():
    datas = request.form # get elements from form

    print('\n\t>>> MESSAGE: [Datas received by form 2]\n') # console message
    for arg, value in datas.items():
        print(f'\t{arg}: {value}')

    username = datas.get('username')
    password = datas.get('password')

    permission = sql_bdd.logIn(username, password) # check the presence in datas

    if permission:
        userdatas = {}
        key = ['firstname', 'lastname', 'birthday', 'phone', 'pseudo']

        for x in range(len(permission)):
            userdatas[key[x]] = permission[x]
            x += 1

        for key, value in userdatas.items():
            print(f'\t{key}: {value}')

        print(f'\n\t>>> MESSAGE: [{username} is connected]\n') # console message

        return render_template('userpage.html', fname=userdatas['firstname'], lname=userdatas['lastname'], pseudo=userdatas['pseudo'])
    else:
        print('non')
        return render_template('connection.html')
# ////////////////////////////////

# Execute the app
if __name__ == '__main__':
    app.run(debug=True)