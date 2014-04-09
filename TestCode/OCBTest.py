from ocb.aes import AES
from ocb import OCB
from os import urandom


#A45F5FDEA5C088D1D7C8BE37CABC8C5C
#DEADBEEFAFBFCFDFFF0F1F2F3F4F5F6F

#params
plaintext = bytearray('Dit is mijn belangrijke tekst')
header = bytearray('Afzender: user182@qet.be')
key = bytearray().fromhex('A45F5FDEA5C088D1D7C8BE37CABC8C5C \
DEADBEEFAFBFCFDFFF0F1F2F3F4F5F6F')
nonce = bytearray(range(16)) #willekeurig 1-malig getal
#end params

#init
if len(key) == 16:
    aes = AES(128)
    print "Using AES 128 bit"
elif len(key) == 32:    
    aes = AES(256)
    print "Using AES 256 bit"
ocb = OCB(aes)

print"PT = " + plaintext 

#maak nonce uniek dmv os.urandom(n)
for index in range(16):
    nonce[index] = urandom(1) 

ocb.setNonce(nonce)
print"Nonce = " + "".join(map(lambda b: format(b, "02x"), nonce))

ocb.setKey(key)
print"Key = " + "".join(map(lambda b: format(b, "02x"), key))
print "\n"

#encrypt
print "Encrypting in AES-OCB mode:..."
(tag,ciphertext) = ocb.encrypt(plaintext, header)

print "header = ", header
print "Nonce = " + "".join(map(lambda b: format(b, "02x"), nonce))
print "tag=" + "".join(map(lambda b: format(b, "02x"), tag))
print "CT=" + "".join(map(lambda b: format(b, "02x"), ciphertext)) 
print "\n"


#decrypt
print "Decrypting in AES-OCB mode..."
ocb.setNonce(nonce)
(isValid, plaintext2) = ocb.decrypt(header,ciphertext,tag)
if isValid == True:
    print "Is Valid  = ", isValid
    print "Plaintext = ", str(plaintext2)
else:
    print "CT has been tampered with!"


