import os, sys
MORSE_CODE_DICT = {
     'A' : '.-',
     'B' : '-...',
     'C' : '-.-.',
     'D' : '-..',
     'E' : '.',
     'F' : '..-.',
     'G' : '--.',
     'H' : '....',
     'I' : '..',
     'J' : '.---',
     'K' : '-.-',
     'L' : '.-..',
     'M' : '--',
     'N' : '-.',
     'O' : '---',
     'P' : '.--.',
     'Q' : '--.-',
     'R' : '.-.',
     'S' : '...',
     'T' : '-',
     'U' : '..-',
     'V' : '...-',
     'W' : '.--',
     'X' : '-..-',
     'Y' : '-.--',
     'Z' : '--..',
     '.' : '.-.-.-',
     ',' : '--..--',
     '?' : '..--..',
     '/' : '-..-.',
     '@' : '.--.-.',
     '1' : '.----',
     '2' : '..---',
     '3' : '...--',
     '4' : '....-',
     '5' : '.....',
     '6' : '-....',
     '7' : '--...',
     '8' : '---..',
     '9' : '----.',
     '0' : '-----',
     }

#encryptor  for text to morse Code
#when entering text need to put text  into apostrofs.
def encryptor(text):
     encrypted_text = " "
     for letters in text:
          print(letters)
          if letters != " ":
               encrypted_text = encrypted_text + MORSE_CODE_DICT.get(letters) + " "
               print(encrypted_text)
          else:
               encrypted_text = encrypted_text + " "
     print(text)
     print(encrypted_text)

#decryptor for morse code to text_to_decrypt
#it take morse code and change to text.

def decryptor(text):
     key_list = list(MORSE_CODE_DICT.keys())
     val_list = list(MORSE_CODE_DICT.values())
     text += " "
     morse = ""
     normal = ""
     print(len(text)) #this print the length of the input text
     for letters in text:
          if letters != " ":
               morse = morse + letters
               space_found = 0

          else:
               space_found += 1
               if space_found == 2:
                    normal = normal + ""
               else:
                    normal = normal + key_list[val_list.index(morse)]
                    morse = ""
     print(normal)


print("\n\n\n\t\t\tMorse Code Encrypor And Decryptor..")
change = input("\n\t\tChoose 'E' To Encrypt Or 'D' To Decrypt :")

if change == 'E' or change == 'e':
    text_to_encrypt = input("Enter Some Text To change to morse code : ").upper()
    encryptor(text_to_encrypt)
else :
     text_to_decrypt = input("Enter Morse Code To change to text  : ")
     decryptor(text_to_decrypt)


with open('test.txt', 'a') as f:
    f.writelines('input was'+ ' ' + change  + '\n')
    f.writelines('\n')
    if (change == 'E' or change == 'e'):
        f.writelines('text input was'+ ' ' + text_to_encrypt + '\n')
        f.writelines('\n')
        #f.writelines('result of your input is' + '' + morse )
    else:
        f.writelines('input morse code was' + ' ' + text_to_decrypt + '\n')
        f.writelines('\n')
        #f.writelines('result of your input is' + ' ' + text )
