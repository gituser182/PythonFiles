#!/usr/bin/env python

"""
Oefening op OCB-AES256
Voordeel OCB-AES : Encypting/Decrypting + Authentication
Bron             : http://www.cs.ucdavis.edu/~rogaway/ocb/
"""
#import -------------------------------------------------------------
from ocb.aes import AES
from ocb import OCB
from os import urandom   #voor betere PRNG

#--------------------------------------------------------------------
__author__ = "user182"
__copyright__ = "Copyright 2014"
__credits__ = ["http://www.cs.ucdavis.edu/~rogaway/ocb/ocb-back.htm"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "user182"
__email__ = "user182@qet.be"
__status__ = "Alpha Mar 11, 2014"
#--------------------------------------------------------------------

#params -------------------------------------------------------------
plaintext = bytearray('Dit is mijn belangrijke tekst')
header = bytearray('Sender is user182@qet.be')
#---
key = bytearray().fromhex('A45F5FDEA5C088D1D7C8BE37CABC8C5C \
DEADBEEFAFBFCFDFFF0F1F2F3F4F5F6F') #32 Hex-bytes
nonce = bytearray(range(16)) #willekeurig 1-malig getal
#end params ---------------------------------------------------------

#Definitie van main() -----------------------------------------------
def main():
    """
    de main body met een uitwerking van OCB-AES256
    """
    #init de sleutel: moet 16 of 32 bytes zijn
    if len(key) == 16:
        aes = AES(128)
        print "Using AES 128 bit"
    elif len(key) == 32:    
        aes = AES(256)
        print "Using AES 256 bit"
    ocb = OCB(aes)

    #toon de PlainText
    print"PT = " + plaintext 

    #maak nonce uniek dmv os.urandom(n) en toon in HEX
    for index in range(16):
        nonce[index] = urandom(1) #1 => 1 rnd byte

    ocb.setNonce(nonce)
    print"Nonce = " + "".join(map(lambda b: format(b, "02x"), nonce))

    #toon Key in HEX
    ocb.setKey(key)
    print"Key = " + "".join(map(lambda b: format(b, "02x"), key))
    print "\n"

    #encrypt --------------------------------------------------------
    print "Encrypting in AES-OCB mode:..."
    (tag,ciphertext) = ocb.encrypt(plaintext, header)

    print "header = ", header
    print "Nonce = " + "".join(map(lambda b: format(b, "02x"), nonce))
    print "tag=" + "".join(map(lambda b: format(b, "02x"), tag))
    print "CT=" + "".join(map(lambda b: format(b, "02x"), ciphertext)) 
    print "\n"

    #decrypt --------------------------------------------------------
    print "Decrypting in AES-OCB mode..."
    ocb.setNonce(nonce)
    (isValid, plaintext2) = ocb.decrypt(header,ciphertext,tag)
    if isValid == True:
        print "Is Valid  = ", isValid
        print "Plaintext = ", str(plaintext2)
    else:
        print "CT has been tampered with!"

    
#code steeds helemaal onderaan te plaatsen als app ipv module -------
if __name__ == '__main__':
    main()
