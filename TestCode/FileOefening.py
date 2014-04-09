#!/usr/bin/env python

"""
Oefening op gebruik van files
"""
from os import urandom

#--------------------------------------------------------------------
__author__     = "user182"
__copyright__  = "Copyright 2014, "
__credits__    = ["Guido"]
__license__    = "GPL"
__version__    = "1.0.0"
__maintainer__ = "user182"
__email__      = "user182@qet.be"
__status__     = "Alpha Mar 05, 2014"
#--------------------------------------------------------------------

def SchrijfFile(EenFile):
    myfile = open(EenFile,'w')
    myfile.write('Eerste lijn\n')
    myfile.write('Tweede lijn\n')
    myfile.close()
    
def LeesFile(EenFile):
    #lijn per lijn inlezen
    myfile = open(EenFile,'r')
    while True:
        EenLijn = myfile.readline()
        if len (EenLijn) == 0:
            break   #einde van de file
        print EenLijn,  # , op't laatste om CR tegen te gaan
    myfile.close()
    
def LeesFileInList(EenFile):
    #list maken van strings
    LijnList = []  #start met lege lijst
    myfile = open (EenFile,'r')
    LijnList = myfile.readlines()
    myfile.close()
    return LijnList

def LeesGanseFile(EenFile):
    #lees de ganse file
    myfile = open(EenFile,'r')
    content = myfile.read()
    myfile.close()
    return content

def FileCopy(fromFile, toFile):     #binair lezen van een file
    frfile = open(fromFile,'rb')   # 'rb' = read binary
    tofile = open(toFile,'wb')     # 'wb' = write binary
    
    while True:
        buf = frfile.read(1024)     #lees per 1024 bytes
        if len(buf) ==0:            #lege buffer?
            break
        tofile.write(buf)
       
    tofile.close()
    frfile.close()
    
def ReadBinaryFileIntoByteArray(EenFile):
    binfile = open(EenFile, 'rb')
    ba = ""
    while True:
        buf = bytearray(binfile.read(1024))
        if len(buf) == 0:
            break
        ba = ba + bytearray(buf) #omzetten naar een bytearray
    binfile.close()
    return ba

def CreateRandomFile(EenFile, lengte):
    binfile = open(EenFile,'wb')
    buf = ""
    for i in range(lengte):
        binfile.write(urandom(1))
    binfile.close()
    
def CreateFile(DataFile, Inhoud):
    txtFile = open(DataFile,'w')
    txtFile.write(Inhoud)
    txtFile.close()
    


    
    

#steeds als voorlaatste
def main():
    print "Programmed by %s" % __author__
    PTFile = '/home/user1/PythonFiles/OCBPTFile.rnd'
    KeyFile = '/home/user1/PythonFiles/OCBKeyFile.rnd'
    NonceFile = '/home/user1/PythonFiles/OCBNonceFile.rnd'
    HeaderFile = '/home/user1/PythonFiles/OCBHeaderFile.txt'
    ToFile = '/home/user1/PythonFiles/OCBFinal.rnd'
    #SchrijfFile(MijnFile)
    #LeesFile(MijnFile)
    #l = LeesFileInList(MijnFile)
    #print "List=",l
    #c = LeesGanseFile(MijnFile)
    #print "content = " , c
    #print "content Split = ",c.split()
    #FileCopy(MijnFile, ToFile)
    
    
    #oefening voor OCB-AES256
    CreateRandomFile(PTFile, 4096)  #te vercijferen info = PKI-keyfile
    CreateRandomFile(KeyFile, 32)
    CreateRandomFile(NonceFile, 16)
    CreateFile(HeaderFile,"Afzender = user182")
    
    
    
    
    
    
    print "***einde"
    
#steeds helemaal onderaan te plaatsen als app ipv module
if __name__ == '__main__':
    main()