logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text,shift_ammount,cipher_direction):
    end_text = ""
    if cipher_direction == 'decode':
        shift_ammount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            # if cipher_direction == 'decode':
            #     new_position = position - shift_ammount
            # elif cipher_direction == 'encode':
            new_position = position + shift_ammount
            new_char = alphabet[new_position]
            end_text += new_char
    print(f"your {cipher_direction} message is {end_text}")


should_end = False
while not should_end:
    direction = input("Enter you direction ? type 'encode'for encrypt or type 'decode'for decrypt\n")
    text = input("type your message\n").lower()
    shift = int(input("tye the shift number\n"))

    shift = shift % 26
    caesar(start_text=text,shift_ammount=shift,cipher_direction=direction)

    restart = input("type 'yes' if you want to go again otherwise type 'no'\n").lower()
    if restart == 'no':
        should_end = True
        print("goodbye")
    elif restart !='yes':
        should_end = True
        print("fuck off")

