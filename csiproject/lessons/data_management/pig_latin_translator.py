#Takes a string input(only alpha characters) and convert the input into pig latin

'''
If the word starts with a vowel, such as the word 'ate', the translation is 'ateway'

If it starts with a letter that is not a vowel, then:
1.Remove the first letter
2.Append the letter to the end of the word
3.Append 'ay' to the end of the word

frog = rogfay
'''

def convert_word(text):
    """
    Converts a word to pig latin
    :param text: single word, only alpha characters
    :return: translated word in pig latin
    """
    vowels = ['a','e','i','o','u']
    new_word = ''
    if text[0].lower() in vowels:
        new_word = text + 'way'
    else:
        new_word = text[1:] + text[0].lower() + 'ay'
    return new_word

def choose_process():
    print('Do you want to convert a word or a sentence?:')
    print('Select "W" for a word or "S" for a sentence')
    choice = input()
    choice = choice.upper()
    if choice == "W":
        chooseWord()
    elif choice == "S":
        chooseSentence()
    else:
        print('Invalid Input, please try again')
        choose_process()

def chooseWord():
    text = input('Enter a word for translation:')
    if text.isalpha():
        translated_word = convert_word(text)
        print('The translated word',text,'translates to',translated_word,'in pig latin.')
    else:
        print('You made an error in your input, please try again. Enter a single word for validation')
        chooseWord()

choose_process()

