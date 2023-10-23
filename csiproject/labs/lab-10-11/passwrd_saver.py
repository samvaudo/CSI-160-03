import pickle
import sys
import pwnedpasswords

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
"""
edit_dict = {'1':'username',
             '2':'password',
             '3':'url',
             '4':'exit'}

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
    global entries, encryption_key
    entries, encryption_key = pickle.load(open(password_file_name, "rb"))


def save_password_file():
    """Saves a password file.  The file will be created if it doesn't exist.

    :param file_name (string) The file to save.
    """
    pickle.dump((entries, encryption_key), open(password_file_name, "wb"))


def add_entry():
    """Adds an entry with an entry title, username, password and url

    Includes all user interface interactions to get the necessary information from the user
    """
    title = input("What is the title for this addition?:")
    username = input("What is the username for this addition?:")
    passw = input("And the password?:")
    passencrypt = password_encrypt(passw, encryption_key)
    url = input("And what is the URL for the login?:")
    entries[title] = {'username': username, 'password': passencrypt, 'url': url}
    print("Entry Saved!")


def print_entry():
    """Asks the user for the name of the entry and prints all related information in a pretty format. Includes all information about an entry.
    """
    work_entry = {}
    work_user = ""
    work_pass_encrypted = ""
    work_pass_decrypted = ""
    work_url = ""

    print("Which entry do you want to lookup the information for?")
    for key in entries:
        print(key)
    entry = input('Enter entry name: ')
    if entry in entries:
        work_entry = entries[entry]
        work_user = work_entry['user']
        work_pass_encrypted = work_entry['password']
        work_pass_decrypted = password_decrypt(work_pass_encrypted, encryption_key)
        work_url = work_entry['url']
        print("Data found!")
        print("The data for entry", entry)
        print("Username:", work_user)
        print("Password:", work_pass_decrypted)
        print("URL:", work_url)
    else:
        print("Data entry not found (Maybe you misspelled it?). Aborting....")

    """Asks the user for the name of an entry, and what variable to edit. Asks in a pretty format
    """
    work_entry = {}
    work_user = ""
    work_pass_encrypted = ""
    work_pass_decrypted = ""
    work_url = ""

    print("Which entry do you want to lookup the information for?")
    for key in entries:
        print(key)
    entry = input('Enter entry name: ')
    if entry in entries:
        if entry in entries:
            work_entry = entries[entry]
            work_user = work_entry['user']
            work_pass_encrypted = work_entry['password']
            work_pass_decrypted = password_decrypt(work_pass_encrypted, encryption_key)
            work_url = work_entry['url']
            print("Data found!")
            print("The data for entry", entry)
            print("Username:", work_user)
            print("Password:", work_pass_decrypted)
            print("URL:", work_url)
            while True:
                choice = input(edit_text)
                if choice in edit_dict and edit_dict[choice]:
                    if choice == 4:
                        print("Canceling...")
                        break
                    elif choice == 2:
                        new_pass = input("Enter new password to override?:")


        else:
            print("Data entry not found (Maybe you misspelled it?). Aborting....")

def del_entry():
    """Asks the user for the name of an entry, and to confirm deleting it. Asks in a pretty format
    """
    pass

def end_program():
    sys.exit()


def print_dictionary():
    print(entries)


menu_dict = {'1': load_password_file,
             '2': add_entry,
             '3': print_entry,
             '4': edit_entry,
             '5': del_entry,
             '6': save_password_file,
             '7': end_program,
             '8': print_dictionary}

while True:
    user_choice = input(menu_text)
    if user_choice in menu_dict and menu_dict[user_choice]:
        menu_dict[user_choice]()
    else:
        print('Not a valid choice')
