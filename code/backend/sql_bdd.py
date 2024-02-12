# Codage: utf-8
import sqlite3

# ////////// functions ///////////
def signIn(pseudo, password, email, firstname, lastname, birthday, phone):
    """
    Function to register a new user.

    Args:
        pseudo (str): User's pseudonym.
        password (str): User's password.
        email (str): User's email address.
        firstname (str): User's first name.
        lastname (str): User's last name.
        birthday (str): User's birthday.
        phone (str): User's phone number.

    Returns:
        bool: True if registration is successful, False otherwise.
    """
    connection = sqlite3.connect('code/backend/BDD.db')  # connection to the database
    cursor = connection.cursor()

    # List all pseudos and emails
    cursor.execute("SELECT pseudo, email FROM Members")
    results = cursor.fetchall()
    datas = [item for result in results for item in map(str, result)]

    # Check datas received
    if (pseudo in datas) or (email in datas):
        # Don't allow registration
        print("\n\t>>> MESSAGE: [Registration not allowed]")
        connection.close()
        return False
    else:
        # Insert the user into Members table
        print("\n\t>>> MESSAGE: [Registration allowed]")
        cursor.execute("INSERT INTO Members (pseudo, password, email) VALUES (?, ?, ?)", (pseudo, password, email))
        user_id = cursor.lastrowid  # get the last ID
        # Insert the user's information into Members_info table
        cursor.execute("INSERT INTO Members_infos (user_id, firstname, lastname, birthday, phone) VALUES (?, ?, ?, ?, ?)", (user_id, firstname, lastname, birthday, phone))
        print(f'\n\t>>> MESSAGE: [{firstname} {lastname} alias "{pseudo}" added]')
        # Valid and stop the connection
        connection.commit()
        connection.close()
        return True

def logIn(username, password):
    """
    Function to authenticate a user.

    Args:
        username (str): User's email or pseudonym.
        password (str): User's password.

    Returns:
        Union[bool, list]: List of user data if authentication is successful, False otherwise.
    """
    connection = sqlite3.connect('code/backend/BDD.db')  # connection to the database
    cursor = connection.cursor()

    # Check datas received
    res = cursor.execute('SELECT Members_infos.firstname, Members_infos.lastname, Members_infos.birthday, Members_infos.phone, Members.pseudo FROM Members_infos JOIN Members ON Members_infos.user_id = Members.user_id WHERE (Members.email = ? OR Members.pseudo = ?) AND Members.password = ?', (username, username, password))
    results = res.fetchall()
    userdatas = [item for result in results for item in map(str, result)]

    if len(results) > 0:
        # Allow connection
        print("\n\t>>> MESSAGE: [Connection allowed]")
        connection.close()
        return userdatas
    else:
        # Don't allow connection
        print("\n\t>>> MESSAGE: [Connection not allowed]")
        connection.close()
        return False
# ////////////////////////////////

# //////////// Tools /////////////
def delete(tables_list):
    """
    Function to delete data from specified tables.

    Args:
        tables_list (list): List of table names to be deleted.

    Returns:
        None
    """
    connection = sqlite3.connect('code/backend/BDD.db')
    cursor = connection.cursor()
    for table in tables_list:
        cursor.execute(f"DELETE FROM {table};")

    connection.commit()
    x = len(tables_list)
    print(f"{x} tables were deleted.")

def delete_table():
    """
    Function to interactively delete tables from the database.

    Returns:
        None
    """
    instruction = input('Names of tables to delete : ').split()
    delete(instruction)
# ////////////////////////////////