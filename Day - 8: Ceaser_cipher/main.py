import art
#project - Ceaser Cipher
#general
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#combined function
def ceaser_cipher(input_text, shift_amount):   
    code = [] 
    if direction == 'decode': #change shift to negative if decoding
        shift_amount *= -1
    for letter in input_text:
        if letter not in alphabet: #for spaces and letters
            code.append(letter)
        else:
            before_shift = alphabet.index(letter) #common for both
            after_shift = before_shift + shift_amount
            #debugging for out of range
            while after_shift not in range (alphabet_length):
                if direction == 'encode':
                    after_shift = abs(alphabet_length - after_shift)
                elif direction == 'decode':
                    after_shift = alphabet_length + after_shift
            code.append(alphabet[after_shift])
    print(f"Here is your {direction}d text: {''.join(code)}")
    

print(art.logo) #add logo

yes = True #restart value
while yes == True:
    #take input
    alphabet_length = len(alphabet)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    #call function
    ceaser_cipher(text,shift)
    #ask user for restart
    check = input("Do you want to start the cipher? ").lower()
    if check == 'yes':
        yes = True
    else:
        yes = False    









