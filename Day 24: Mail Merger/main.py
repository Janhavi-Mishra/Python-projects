# TODO: Create a letter using starting_letter.txt

with open("./Input/Letters/starting_letter.txt") as starting_letter:  # opened the starting letter
    contents = starting_letter.readlines()  # saved each line an object in a list

    with open("./Input/Names/invited_names.txt") as invited_names:  # opened the names inside
        names = invited_names.readlines()  # saved each name an object in a list

        i = 0  # flag
        for name in names:
            names[i] = name.strip()  # removed spaces from names and saved again
            name = names[i]
            i = i + 1

            with open(f"./Output/ReadyToSend/{name}.txt", mode='w') as new_file:  # created files for each name inside
                # for loop
                contents[0] = f"Dear {name},\n"  # added changes to the salutation
                for x in contents:  # added all the objects in contents to the files
                    new_file.write(x)



