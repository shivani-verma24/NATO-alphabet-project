import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter : row.code for (index, row) in data.iterrows()}


def generate_phonetic():

    word = input("Enter a word: ").upper()
    try:
        word_code = [alphabet_dict[letter] for letter in word]

    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()

    else:
        print(word_code)

generate_phonetic()


# Project by Shivani Verma
