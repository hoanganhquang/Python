import pandas

data = pandas.read_csv("nato.csv")

new_dict = {row.letter: row.code for (index, row) in data.iterrows()}

name_input = input("Enter a word: ").upper()

new_name = [new_dict[word] for word in name_input]
print(new_name)
