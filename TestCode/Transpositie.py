#!/usr/bin/env python3

#transpositie cipher - met aanmaak van functies (def)

def main():
    myMessage = 'Common sense is not so common.'
    myKey = 8
    Ciphertext = encryptMessage(myKey, myMessage)
    print(Ciphertext,'|') #de | om einde CT aan te duiden
    
def encryptMessage(key,message):
    Ciphertext = [''] * key #array (grootte = key) met lege veld
    
    for col in range(key): #loop door elke kolom
        pointer = col
        
        while pointer < len(message):
            Ciphertext[col] +=  message[pointer]
            pointer += key #ophogen pointer = 1 rijtje gelezen
        
    
    return ''.join(Ciphertext) #hetgeen de f(x) aflevert


#Als deze module wordt gerund, call main op de volgende manier
if __name__ == '__main__':
    main()
    
    
