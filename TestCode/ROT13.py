import pyperclip
print('ROT13\n\n')

#Het letterset waarmee gewerkt wordt
LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

#zeer uitgebreide lijst met aanvaardbare char

#De containers waarin PT en CT worden geplaatst
message = 'This is my PASSWORD'  #PT
#message = "auv!-v!-z'-]N``d\_Q"  #with key = 13
translated = '' #CT

#De sleutel (ROT13)
key = 13
mode = 'E' #E = Encrypt  D = Decrypt


#--------
#message = message.upper()
print ('PT = ' + message)

#loop door het bericht en ctrl of de symbolen
#voorkomen in het set LETTERS
for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol) #haal de ASCII op van het symbol
        if mode == 'E':
            num = num + key
        elif mode == 'D':
            num = num -key

        #opgelet voor overflow in range van LETTERS (1..lengte(Letters))  wrap-around
        if num >=len(LETTERS):
            num = num - len(LETTERS)
        elif num<0:
            num = num + len(LETTERS)

        #hier volgt de eigenlijke cijfering
        #neem letter uit LETTERS die key plaatsen verder staat in de array
        translated = translated + LETTERS[num]    
    else:
        #symbool staat niet in LETTERS - neem gewoon over in translated
        translated = translated + symbol
        
print ('CT = ' + translated)
pyperclip.copy(translated)
#---------- einde


print ('Brute Force attack on "%sCT"'%translated)

for k in range(len(LETTERS)): #doorloop elke mogelijke letterreeks
    broken = ''
    
    for symbol in translated: #gebruik elk symbool uit CT
        if symbol in LETTERS: #staat het in LETTERS?
            num = LETTERS.find(symbol) #geef de overeenkomende ASCII waarde
            num = num - k              #trek de sleutel 'k' er vanaf
            
            #overflow tegengaan
            if num <0:
                num = num + len(LETTERS)
                
            broken = broken + LETTERS[num] #vorm ontcijferd bericht
            
        else:
            broken = broken + symbol
            
    print ('Key #%s: %s'%(k, broken))
    
    
    


