with open("Input/Names/invited_names.txt") as file1:
    name = file1.readlines()

with open("Input/Letters/starting_letter.txt") as file:
    letter = file.read()
    for i in name:
        directory = f"Output/ReadyToSend/letter_for_{i.strip()}.docx"
        new_letter = letter.replace("[name]", i)
        with open(directory, mode="w") as file2:
            file2.write(new_letter)
