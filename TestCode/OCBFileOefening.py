#!/usr/bin/env python

"""
Oefening op gebruik van OCB-AES256
"""
from ocb.aes import AES
from ocb import OCB
from os import urandom
from os import remove
import datetime
import hashlib
import uuid   #unieke uuid genereren
import pickle #serialize objects in memory naar file e.o.
import shutil #file copy

#--------------------------------------------------------------------
__author__     = "user182"
__copyright__  = "Copyright 2014"
__credits__    = ["Guido"]
__license__    = "GPL"
__version__    = "1.0.0"
__maintainer__ = "user182"
__email__      = "user182@qet.be"
__status__     = "Beta 1 - Mar 18, 2014"
#--------------------------------------------------------------------

def ReadBinaryFileIntoBuffer(EenFile): #-----------------------------
    """
    leest een binary file in en plaatst de inhoud in een buffer
    """
    res = ""
    binfile = open(EenFile, 'rb')  #leesmode read-only binary
    while True:
        buf = binfile.read(1024)
        if len(buf) == 0:
            break
        res = res + buf
    binfile.close()
    return res #-----------------------------------------------------

def ReadBinaryFileIntoByteArray(EenFile): #--------------------------
    """
    lees een binary file en steek de inhoud in een bytearry
    """
    binfile = open(EenFile, 'rb') #leesmode read-only binary
    ba = ""                       #bytearray is leeg
    while True:
        buf = bytearray(binfile.read(1024))
        if len(buf) == 0:
            break
        ba = ba + bytearray(buf) #omzetten naar een bytearray
    binfile.close()
    return ba #------------------------------------------------------

def CreateRandomFile(EenFile, lengte): #-----------------------------
    """
    Maak een file van een gekende lengte en vul met random inhoud 
    """
    binfile = open(EenFile,'wb')  #schrijfmode binary
    for i in range(lengte):
        binfile.write(urandom(1)) #urandom voor degelijke PRNG
    binfile.close() #------------------------------------------------
    
def CreateFile(DataFile, Inhoud): #----------------------------------
    """
    Schrijf de Inhoud (van een string) naar een file
    """
    txtFile = open(DataFile,'w') #open om te schrijven
    txtFile.write(Inhoud)
    txtFile.close() #------------------------------------------------
    
def WriteList(DataFile,lijst): #-------------------------------------
    """
    Schrijf een list naar schijf dmv serialising (import pickle)
    """
    binfile = open(DataFile, 'wb') #binary mode voor pickle
    #gebruik pickle om te serializen
    pickle.dump(lijst, binfile) #duw de list in een file
    binfile.close() #------------------------------------------------
 
def ReadList(DataFile): #--------------------------------------------
    """
    Haal via serialising de inhoud uit een file en stop in een list
    """
    binfile = open(DataFile, 'rb') #binary mode voor pickle
    lijst = pickle.load(binfile) #gebruik pickle om te serializen
    binfile.close()
    return lijst #---------------------------------------------------

def WriteBinaryFile(EenFile, Inhoud): #------------------------------
    """
    Schrijf een binary file naar disk 
    """
    binfile = open(EenFile,'wb') #schrijfmode binary
    for s in Inhoud:
        binfile.write(s) #Schrijf Inhoud (byte/byte) naar disk 
    binfile.close() #------------------------------------------------

    
def ZetStringOmInByteArray(aString): #-------------------------------
    """
    Neem een string en zet deze om in een bytearray
    """
    rValue = bytearray(len(aString))  #initialiseer array
    for index in range(len(aString)): #invullen
        rValue[index] = aString[index]
    return rValue #--------------------------------------------------

def ToonByteArrayInHex(anArray): #-----------------------------------
    """
    info gehaald van stackoverflow.com om bytearray te tonen in HEX
    """
    return "".join(map(lambda b: format(b, "02x"), anArray))#--------

def hash_password(password, salt = None): #--------------------------
    """
    Gebruik van een salt alvorens het pwd te hashed
    Geeft zowel een hash af alsook de salt
    """
    if salt is None: #default waarde is None  
        #Dan moet de param niet worden ingevuld in de call naar de fx
        #en bepalen we zelf een salt-waarde
        salt = uuid.uuid4().hex #uuid4 = random uuid
        
    #vergroot het pwd door er een 'salt' aan te plakken voor de sha    
    hashedpwd = hashlib.sha256(password + salt).hexdigest()
    return(hashedpwd, salt) #----------------------------------------

def verify_password(password, hashed_password, salt): #--------------
    """
    Nagaan of de berekende hash wel van het pwd + salt komen
    Als de berekening van pwd + salt dezelfde waarde oplevert 
    als de meegegeven hash is het in orde
    """
    rehashed = hash_password(password, salt) #geeft salt mee
    return rehashed == hashed_password #-----------------------------

def OCBFileDecrypt(aKeyFile, aCTFile, aPTFile): #--------------------
    """
    File ontcijferen. De file is een stream (pickle) van een list.
    De volgorde van de list is: 
    (0)hdr, (1)salt, (2)nonce, (3)tag, (4)CT
    Gebruik de KeyFile en haal de salt op. Hash om key te maken
    """
    resultaat = False
    res = ["invalid","invalid"]
    KeyBuf = ReadBinaryFileIntoBuffer(aKeyFile)
    #resultaat lijst: volgorde =  hdr, salt, nonce, tag, CT
    lijst = ReadList(aCTFile)
    
    if len(KeyBuf) == 32:
        hashedPwd, salt2 = hash_password(KeyBuf,lijst[1])
            
        #input naar hexadecimaal: afbreken key 
        #32bytes (gebruik van AES-256 eist 32 bytes als key) 
        #nonce = steeds 16 bytes
        OCBNonceStr  = lijst[2]    
        OCBHeaderStr = lijst[0]
        OCBCTStr     = lijst[4]
        OCBTagStr    = lijst[3]
        OCBKeyStr    = hashedPwd[0:32]
        
        #omzetten naar bytearray
        OCBKey   = bytearray(OCBKeyStr)
        OCBCT    = bytearray(OCBCTStr)
        OCBNonce = bytearray(OCBNonceStr)
        OCBHdr   = bytearray(OCBHeaderStr)
            
        #ontcijfering 
        aes = AES(256)
        ocb = OCB(aes)    
        ocb.setKey(OCBKey)    
        ocb.setNonce(OCBNonce)
        (isValid, PT2)= ocb.decrypt(OCBHdr, OCBCT, OCBTagStr)
        resultaat = isValid
        if isValid == True:
            res[0] = lijst[0].decode("hex")
            res[1] = PT2.decode("hex")
            #schrijf de PT naar File
            #WriteBinaryFile(aPTFile, res[1])            
    else:
        print "KeySize must be 32 bytes (AES-256)"
        
    return resultaat, res #------------------------------------------    


def OCBFileEncrypt(aKeyFile, aHeaderFile, aNonceFile, aPTFile, aDataFile):
    resultaat = False
    KeyBuf = ReadBinaryFileIntoBuffer(aKeyFile)
    HDRBuf = ReadBinaryFileIntoBuffer(aHeaderFile)
    NonBuf = ReadBinaryFileIntoBuffer(aNonceFile)
    PTBuf  = ReadBinaryFileIntoBuffer(aPTFile)
    
    if (len(KeyBuf)==32) and (len(NonBuf)==16):
        (SaltedKey, salt) = hash_password(KeyBuf) #geef ook de salt weer
        OCBKeyStr = SaltedKey[0:32]
        OCBNonceStr = NonBuf
        OCBHeaderStr = HDRBuf.encode("hex")
        OCBPTStr = PTBuf.encode("hex")  
            
        #omvormen naar bytearray
        OCBKey   = bytearray(OCBKeyStr)
        OCBPT    = bytearray(OCBPTStr)
        OCBNonce = bytearray(OCBNonceStr)
        OCBHdr   = bytearray(OCBHeaderStr)
        
        #vercijfering   
        aes = AES(256)
        ocb = OCB(aes)
        ocb.setKey(OCBKey)
        ocb.setNonce(OCBNonce)
        (tag,CT) = ocb.encrypt(OCBPT, OCBHdr)
               
        #resultaat in een list meegeven: volgorde =  hdr, salt, nonce, tag, CT
        res= []
        res.append(OCBHeaderStr) 
        res.append(salt)
        res.append(OCBNonceStr)    
        res.append(tag)
        res.append(CT)        
        
        #wis de oorspronkelijke PT-file van schijf
        wait = raw_input("Press ENTER to continue")
        remove(aPTFile) 
        resultaat = True
        
    else:    
        print "KeySize must be 32 bytes (AES-256)"
        print "Nonce must be 16 bytes"
        
    return resultaat, res   
        
       
def OCBStringEncrypt(aKey, aHeader, aPT):
    #SaltHash van aKey
    (SaltedKey, salt) = hash_password(aKey) #geef ook de salt weer
    NonceUUID = uuid.uuid4().hex #random nummer om een nonce te maken
        
    #input naar hexadecimaal: afbreken key = 32bytes (AES256), nonce = 16 bytes
    OCBKeyStr = SaltedKey[0:32]
    OCBNonceStr = NonceUUID[0:16]
    OCBHeaderStr = aHeader.encode("hex")
    OCBPTStr = aPT.encode("hex")  
    
    #omvormen naar bytearray
    OCBKey   = bytearray(OCBKeyStr)
    OCBPT    = bytearray(OCBPTStr)
    OCBNonce = bytearray(OCBNonceStr)
    OCBHdr   = bytearray(OCBHeaderStr)   
    
    #vercijfering   
    aes = AES(256)
    ocb = OCB(aes)
    ocb.setKey(OCBKey)
    ocb.setNonce(OCBNonce)
    (tag,CT) = ocb.encrypt(OCBPT, OCBHdr)
       
    #resultaat in een list meegeven: volgorde =  hdr, salt, nonce, tag, CT
    res= []
    res.append(OCBHeaderStr) 
    res.append(salt)
    res.append(OCBNonceStr)    
    res.append(tag)
    res.append(CT)
    
    return res

def OCBStringDecrypt(pwd, lijst):
    res = ["invalid","invalid"]
    hashedPwd, salt2 = hash_password(pwd,lijst[1])
    
    #input naar hexadecimaal: afbreken key = 32bytes (AES256), nonce = 16 bytes
    OCBNonceStr  = lijst[2]    
    OCBHeaderStr = lijst[0]
    OCBCTStr     = lijst[4]
    OCBTagStr    = lijst[3]
    OCBKeyStr    = hashedPwd[0:32] 

    #omzetten naar bytearray
    OCBKey   = bytearray(OCBKeyStr)
    OCBCT    = bytearray(OCBCTStr)
    OCBNonce = bytearray(OCBNonceStr)
    OCBHdr   = bytearray(OCBHeaderStr)
    
    #ontcijfering 
    aes = AES(256)
    ocb = OCB(aes)    
    ocb.setKey(OCBKey)    
    ocb.setNonce(OCBNonce)
    (isValid, PT2)= ocb.decrypt(OCBHdr, OCBCT, OCBTagStr)
    if isValid == True:
        res[0] = lijst[0].decode("hex")
        res[1] = PT2.decode("hex")
    return res        
        
        
    
#def main() is steeds de voorlaatste def van een Python script ------
def main():
    #haal dtg op en toon op scherm = ctrl of het script wel 'draait'
    now = datetime.datetime.now()
    print "Programmed by %s at %s" % (__author__, now.isoformat())
    
    #self-test van OCB-AES256 -----------------------------------------------------
    
    
    #--- de nodige files ----------------------------------------------------------
    PTFile = '/home/user1/PythonFiles/OCBPTFile.rnd'
    PT2File = '/home/user1/PythonFiles/OCBPTFileCOPY.rnd'
    KeyFile = '/home/user1/PythonFiles/OCBKeyFile.rnd'
    NonceFile = '/home/user1/PythonFiles/OCBNonceFile.rnd'
    HeaderFile = '/home/user1/PythonFiles/OCBHeaderFile.txt'
    ToFile = '/home/user1/PythonFiles/OCBFinal.rnd'
    
    #maak de nodige bestanden aan om de OCB-AES256 te kunnen testen
    CreateRandomFile(PTFile, 4096)  #te vercijferen info 
    shutil.copyfile(PTFile, PT2File)#copy de file om te kunnen vgl
    CreateRandomFile(KeyFile, 32)   #een random Key, grootte = 32 bytes
    CreateRandomFile(NonceFile, 16) #een random nonce, grootte = 16 bytes
    CreateFile(HeaderFile,"Afzender = user182") #een handmatige gekozen Header
    
    #data voor de string-encryptie ------------------------------------------------
    aKey = "Dit is mijn sleutel"
    aHeader = "User182"
    aPT = "Dit is de te beschermen text 1 2 3 4 5 6 7 8 9 0"
    
    print "*** Encoding %s + %s" %(aHeader, aPT)
    resultaat = OCBStringEncrypt(aKey, aHeader, aPT) #in list
    #resultaat is een list : volgorde =  hdr, salt, nonce, tag, CT
    #print "Header=" ,resultaat[0]    
    #print "Salt=", resultaat[1]
    #print "Nonce=" ,resultaat[2]
    #print "Tag=", resultaat[3]
    #print "CT=", resultaat[4]
    
    print "Writing encrypted string to disk"
    WriteList(ToFile,resultaat)
    
    print "Reading encrypted string from disk"
    GelezenList = ReadList(ToFile)
    
    print "*** Decoding the string from list"
    res = OCBStringDecrypt(aKey, GelezenList)
    for item in res:
        print item
    
    #------------------------------------------------------------------------------    
    print "*** OCB File Encrypt ***"
    bValue, listValue = OCBFileEncrypt(KeyFile, HeaderFile, NonceFile, \
    PTFile, ToFile)
    if bValue:
        print "Encryption of PT into CT\nFile %s  \nFile %s" % (PTFile,ToFile)
        WriteList(ToFile,listValue)        
    else:
        print "There was an error during encryption"
        
    #------------------------------------------------------------------------------    
    print "*** OCB File Decrypt ***"
    bValue, ReturnedListValue = OCBFileDecrypt(KeyFile, ToFile, PTFile)
    if bValue:
        print "Decryption of CT into PT\nFile %s  \nFile %s" % (ToFile, PTFile)
        #schrijf de PT naar File
        WriteBinaryFile(PTFile, ReturnedListValue[1])           
    else:
        print "There was an error during decryption"        
    
    #einde main() -----------------------------------------------------------------
    print "*** einde ***"
     
#steeds helemaal onderaan te plaatsen als app ipv module --------------------------
if __name__ == '__main__':
    main()    