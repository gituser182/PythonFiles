import pyperclip

print ('testing the CAESAR/ROT Cipher')

message=input('Typ het te vercijferen bericht:')
key = 3 #ROTx met  x=waarde van key
mode = 'encrypt' #of 'decrypt'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #De toegelaten letters
translated = ''  #bevat eindresultaat


message = message.upper() #zet a..z in hoofdletters

for s in message:
    if s in LETTERS:
        num = LETTERS.find(s) #vind de index van de letter in LETTERS
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        #oplossen waarde nul in range letters
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num<0:
            num = num + len(LETTERS)

        translated = translated + LETTERS[num]

    else:
        translated = translated + s #s komt niet voor in LETTERS

print(translated)
pyperclip.copy (translated)

            

