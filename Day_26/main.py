import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for (_, row) in df.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("What is your name?")
coded = [new_dict.get(character.upper()) for character in name]
print(coded)
