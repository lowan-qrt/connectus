#codind:utf-8
import sqlite3

def signIn(pseudo, password, email, firstname, lastname, birthday, phone):

    connection = sqlite3.connect('backend/BDD.db')
    cursor = connection.cursor()

    pseudos_list = cursor.execute("SELECT pseudo FROM Members")
    emails_list = cursor.execute("SELECT email FROM Members")
    print(f'\npseudos_list:\n{pseudos_list}\nemails_list:\n{emails_list}\n')
    print(str(pseudo), str(email))

    if str(pseudo) in pseudos_list:
        print(f'Pseudo [{pseudo}] already used by another account.')
        return False
    if str(email) in emails_list:
        print(f'Email [{email}] already used by another account.')
        return False
        
    # Insert the user into Members table
    cursor.execute("INSERT INTO Members (pseudo, password, email) VALUES (?, ?, ?)", (pseudo, password, email))
    # Get last ID
    user_id = cursor.lastrowid
    # Insert the users informations into Members_info table
    cursor.execute("INSERT INTO Members_infos (user_id, firstname, lastname, birthday, phone) VALUES (?, ?, ?, ?, ?)",
                (user_id, firstname, lastname, birthday, phone))

    # Valid and stop connection
    print(f'\n\tMESSAGE: {firstname} {lastname} alias @{pseudo} added.\n')
    connection.commit()
    connection.close()

def logIn(id, password):
    pass