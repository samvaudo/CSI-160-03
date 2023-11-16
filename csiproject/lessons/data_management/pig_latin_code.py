#Working with character conversions - words and sentences

'''
ate = ateway is the pig latin translation
frog = rogfay s the pig latin translation
'''

vowels = ['a', 'e', 'i', 'o', 'u']

def convert_word(text):
    if text[0].lower() in vowels:
        new_word = text + "way"
    else:
        new_word = text[1:] + text[0].lower() + 'ay'
    return new_word

    #Change the print to a return

'''
Place convert_sentence below
'''
def convert_sentence(sentence):
    new_sentence = "" #This will hold the pig latin equivalent of the sentence
    length = len(sentence)
    words = sentence.split()
    for word in words:
        new_sentence = new_sentence + convert_word(word) + ' '
    new_sentence = new_sentence[0:-1]
    return new_sentence

def choose_process():
    print('Welcome to the pig latin translator.')
    print('Enter a "W" or word translation or "S" for sentence translation')
    choice = input()
    choice = choice.upper()
    if choice == "W":
        chooseWord()
    elif choice == "S":  #Add this elif to code:
        chooseSentence()
    else:
        print("Good-bye")
        exit()

def chooseWord():
    print('Please enter your word.')
    text = input()
    if text.isalpha:
        print(convert_word(text))
        choose_process()
    else:
        print("Invalid input.")
        choose_process()

def chooseSentence():
    print("Enter your sentence:")
    sentence = input()
    for i in sentence:
        if (i.isalpha() == True or i.isspace() == True):
            print(convert_sentence(sentence))
            choose_process()
        else:
            print("Invalid data.")
            chooseSentence()
choose_process()