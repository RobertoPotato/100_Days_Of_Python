# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("Input/Names/invited_names.txt") as f_names:
    with open("Input/Letters/starting_letter.txt") as f_letter:
        names = f_names.readlines()
        letter = f_letter.read()

        for name in names:
            with open(f"Output/ReadyToSend/letter_to_{name}.txt", "w") as file:
                name = name.strip("\n")
                new_letter = letter.replace("[name]", name)
                file.write(new_letter)
