import pickle
import sys
import pwnedpasswords
import os

# The password list - We start with it populated for testing purposes
entries = {'yahoo': {'username': 'johndoe', 'password': 'cus#u%S tu', 'url': 'https://www.yahoo.com'},
           'google': {'username': 'johndoe', 'password': '`q$$( #tABCD^ %fu#*W  t', 'url': 'https://www.google.com'}}

# The password file name to store the data to
password_file_name = "PasswordFile.pickle"
# The encryption key for the caesar cypher
encryption_key = 16

menu_text = """
What would you like to do:
1. Open password file
2. Add an entry
3. Lookup an entry
4. Edit an entry
5. Delete an entry
6. Save password file
7. Quit program
8. Print dictionary for testing
Please enter a number (1-8)"""

edit_text = """
What do you want to edit?
1. Username
2. Password
3. URL
4. Exit Menu
Please enter a number (1-4):"""

edit_dict = {'1': 'username',
             '2': 'password',
             '3': 'url',
             '4': 'exit'}


def password_encrypt(unencrypted_message, key):
    """Returns an encrypted message using a caesar cypher

    :param unencrypted_message (string)
    :param key (int) The offset to be used for the caesar cypher
    :return (string) The encrypted message
    """
    result_string = ''
    min_limit = 32
    max_limit = 126
    for character in unencrypted_message:
        value = ord(character) - min_limit + key
        value = value % (max_limit - min_limit + 1)
        value = value + min_limit
        result_string = result_string + chr(value)
    return result_string


def password_decrypt(encrypted_message, key):
    """Returns a decrypted message.

    :param encrypted_message (string):
    :param key (int) The offset that was used to encrypt the message
    :return (string): The decrypted message
    """
    return password_encrypt(encrypted_message, -key)


def load_password_file():
    """Loads a password file.  The file must be in the same directory as the .py file

    :param file_name (string) The file to load.  Must be a pickle file in the correct format
    """
    file_name = input("Enter the password file to be loaded(file extension will be auto-filled): ")

    global entries, encryption_key
    try:
        entries, encryption_key = pickle.load(open(file_name+'.pkl', "rb"))
        print("File Loaded!")
    except FileNotFoundError:
        print("File not found. Aborting...")
    except TypeError:
        print("Empty File Name. Aborting....")


def save_password_file():
    """Saves a password file.  The file will be created if it doesn't exist.

    :param file_name (string) The file to save.
    """
    file_name = input("Enter the password file to be saved (No file extension):")
    try:
        pickle.dump((entries, encryption_key), open(file_name+'.pkl', "wb"))
        print("File saved!")
    except FileNotFoundError:
        print("File not found. Aborting....")
    except TypeError:
        print("Empty File Name. Aborting....")


def add_entry():
    """Adds an entry with an entry title, username, password and url

    Includes all user interface interactions to get the necessary information from the user
    :return None
    """
    title = input("What is the title for this addition?:")
    username = input("What is the username for this addition?:")
    passw = input("And the password?:")
    passencrypt = password_encrypt(passw, encryption_key)
    url = input("And what is the URL for the login?:")
    entries[title] = {'username': username, 'password': passencrypt, 'url': url}
    print("Entry Saved!")


def print_entry(entry_name):
    """
    Prints entry data (name, username, password (unencrypted) and url
    :param entry_name: Name of entry
    :return: None
    """
    try:
        work_entry = entries[entry_name]
        work_pass_encrypted = work_entry['password']
        print("Data found!")
        print("The data for entry", entry_name)
        print("Username:", work_entry['username'])
        print("Password:", password_decrypt(work_pass_encrypted, encryption_key))
        print("URL:", work_entry['url'])
    except KeyError: # If entry_name not in entries
        print("Data entry not found (Maybe you misspelled it?). Aborting....")


def lookup_entry():
    """Asks the user for the name of the entry and prints all related information in a pretty format. Includes all information about an entry.
    """
    print("Lookup Entries")
    for key in entries: # lists all entry names
        print(key)
    entry = input('Which entry do you want to lookup the information for?:')
    print_entry(entry)


def edit_username(entry_name):
    """
    Changes a username of the entry_name to what the user wants

    :param entry_name: name of the entry
    :return: True if username changed, False if canceled
    """
    try:
        new_user = input("Enter a new username to override: (to cancel, press ENTER instead of a username)")
        if new_user != '':
            entries[entry_name]['username'] = new_user
            print("Entry Updated!")
            return True
        else:
            print("Empty entry. Aborting....")
            return False
    except KeyError:
        print("An error occurred. Aborting....") # if the input cant be taken for some reason
        return False


def edit_passwd(entry_name):
    """
    Changes a password of the entry_name to what the user wants

    :param entry_name: name of the entry
    :return: True if password changed, False if canceled
    """
    try:
        new_pass = input("Enter new password to override: (to cancel, press ENTER instead of a password)")
        if new_pass != '':
            new_pass_encrypt = password_encrypt(new_pass, encryption_key)
            entries[entry_name]['password'] = new_pass_encrypt
            print("Entry updated!")
            return True
        else:
            print("Empty entry. Aborting....")
            return False
    except KeyError:
        print("An error occurred. Aborting...") # if the input cant be taken for some reason
        return False


def edit_url(entry_name):
    """
    Changes the url of the entry_name to what the user wants
    :param entry_name: name of the entry
    :return: True if url changed, False if canceled
    """
    try:
        new_url = input("Enter a new url to override:")
        if new_url != '':
            entries[entry_name]['url'] = new_url
            print("Entry Updated!")
            return True
        else:
            print("Empty entry. Aborting....")
            return False
    except KeyError:
        print("An error occurred. Aborting....") # if the input cant be taken for some reason
        return False


def edit_entry():
    """Asks the user for the name of an entry, and what variable to edit. Asks in a pretty format
    """
    print("Editing Entries")
    for key in entries:
        print(key)
    entry = input('Which entry do you want to edit?:')
    print_entry(entry)
    while True:
        choice = input(edit_text)
        if choice in edit_dict and edit_dict[choice]:
            if choice == '1': # if tree to determine what edit function to run
                if edit_username(entry):
                    break
                else:
                    continue
            elif choice == '2':
                if edit_passwd(entry):
                    break
                else:
                    continue
            elif choice == '3':
                if edit_url(entry):
                    break
                else:
                    continue
            elif choice == '4':
                print("Canceling...")
                break
            else:
                print("Data entry not found (Maybe you misspelled it?). Aborting....")
                break


def del_entry():
    """Asks the user for the name of an entry, and to confirm deleting it. Asks in a pretty format
    """
    print("Deleting Entries")
    for key in entries:
        print(key)
    entry = input('Which entry do you want to delete?:')
    print_entry(entry)
    try:
        confirmation = input("Delete chosen item?: (y/n):") # CONFIRMATION FOR DELETION
        if confirmation == 'y':
            del entries[entry]
            print("Entry Removed")
        else:
            print("Canceling...")
    except KeyError:
        print("Data entry not found (Maybe you misspelled it?). Aborting....")


def end_program():
    sys.exit()


def print_dictionary():
    print(entries)


menu_dict = {'1': load_password_file,
             '2': add_entry,
             '3': lookup_entry,
             '4': edit_entry,
             '5': del_entry,
             '6': save_password_file,
             '7': end_program,
             '8': print_dictionary}

while True:
    user_choice = input(menu_text)
    if user_choice in menu_dict and menu_dict[user_choice]:
        menu_dict[user_choice]()
        print('\n'*80) # clears screen
    else:
        print('Not a valid choice')
