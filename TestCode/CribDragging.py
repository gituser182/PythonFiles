"""
Oefening : OTP twee maal gebruikt. Vind de PlainText
    A, B = Plain Text
    CT1  = (A xor Key1)
    CT2  = (B xor Key1)
    CT1 xor CT2 = (A xor Key1) xor (B xor Key1)
                = (A xor B) xor (Key1 xor Key1)
                = (A xor B) xor   0
                = (A xor B)

                (y xor y = 0)
                (y xor 0 = y)

    
Opgave: Eenvoudig schema met 8 letters, gebruikte taal is Engels
    binair met 8 letters
    0) 000 = e
    1) 001 = h
    2) 010 = i
    3) 011 = k
    4) 100 = l
    5) 101 = r
    6) 110 = s
    7) 111 = t

    Key1 = slekhirtes (6403125706)                    0|1|2|3|4|5|6|7|8|9
    PlainText A = killhilter  => CT1 = (A xor Key1) = r|s|l|t|e|e|i|k|e|k
    PlainText B = helikesike  -> CT2 = (B xor Key1) = t|l|l|h|i|i|k|r|k|s
    CT1 xor CT2 = Plaintext A xor PlainText B       = i|i|e|s|i|i|h|s|k|r
    Opmerking : op plaats 2 staat in CT1 en CT2 dezelfde letter (l)
                dit kan als Key1 op plaats 2 een '0' (e) is, wat het geval is.

Aanpak:

Crib dragging op de geXORde CT is mogelijk
##
1 Guess a word that might appear in one of the messages
2 Encode the word from step 1 to a hex string
3 XOR the two cipher-text messages
4 XOR the hex string from step 2 at each position of the XOR of the two
  cipher-texts (from step 3)
5 When the result from step 4 is readable text, we guess the English word
  and expand our crib search.
6 If the result is not readable text, we try an XOR of the crib word at
  the next position.
##
"""
#           0    1    2    3    4    5    6    7
letters = ['e', 'h', 'i', 'k', 'l', 'r', 's', 't']

#CT1 en CT2
CT1 = "5647002303"  # ipv rslteeikek
CT2 = "7441223536"  # ipv tllhiikrks
# x = CT1 xor CT2
x =   "2206221635"  # ipv iiesiihskr

#boek met woorden die men hoopt te vonden in de cijfertekst
cribs = ["he", "his", "hit", "her", "the", "heli", "kill", "hitler", "likes", "ike", "likesike", "killhitler"] 

def LettersNaarCijfers(aText):
    """
    Omzetten van letters naar een cijfer. Geeft de index weer van de letter in
    """
    cijfers = ""
    for l in aText:
        if l in letters:
           cijfers = cijfers + str(letters.index(l))#haal de index op in de list
        else:
            print " %s komt niet voor" %l
            break
    return cijfers

def cribdrag(aCrib, anXor):
    """
    cribdragging
    """
    thisCrib = LettersNaarCijfers(aCrib)      #omzetten naar cijfersequentie
    #print "Crib %s ----> thisCrib %s " %(aCrib,thisCrib)
    if len(aCrib)<=len(anXor):                #verplichte controle
        LoopTot = len(anXor) - len(aCrib) + 1 #om overflow tegen te gaan
        #print "Lengte_anXor=%d  Lengte_aCrib=%d, LoopTot=%d" %(len(anXor),len(aCrib),LoopTot)
        
        for i in range(0,LoopTot):
            res = ""
            for j in range(0,len(aCrib)):
                y = int(anXor[j+i]) ^ int(thisCrib[j]) #XOR 
                res = res + letters[y]
                #print "*** i=%d  j=%d  j+i=%d  letter=%s" %(i, j, j+i,letters[y])
            #print "gevonden woord = " , res

            if res in cribs: #volledig deel van gevonden woord
                print"FULL HIT! Crib %s gevonden op i=%d i+j=%d" % (res,i,i+j)
                if res not in hits:
                    hits.append(res)

            for crib in cribs: #deel van een gevonden woord
                if (res.find(crib)>=0) and (res not in cribs):
                    print "PARTIAL HIT! Crib %s is gevonden in %s op i=%d i+j=%d" % (crib, res, i,i+j)
                    if crib not in hits:
                        hits.append(crib)
                if (crib.find(res)>=0) and (res not in cribs):
                    print "PARTIAL HIT! %s komt voor in %s op i=%d i+j=%d" % (res, crib, i,i+j)
                    if crib not in hits:
                        hits.append(crib)
                        

def FindKey(aKey):
    print "testing Word %s" % aKey
    thisWord = LettersNaarCijfers(aKey)      #omzetten naar cijfersequentie

    LoopTot = len(CT1) - len(thisWord) +1     #len(x) = len(CT1) = len(CT2)
    for i in range(0,LoopTot):
        res1 = ""  #PT1
        res2 = ""  #PT2

        for j in range(0,len(thisWord)):
            y = int(CT1[j+i]) ^ int(thisWord[j]) #XOR
            z = int(CT2[j+i]) ^ int(thisWord[j]) #XOR
            print "CT1[%d]=%s  Word[%d]=%s x=%s" % (j+i,x[j+i], j, thisWord[j], letters[y])
            print "CT2[%d]=%s  Word[%d]=%s x=%s" % (j+i,x[j+i], j, thisWord[j], letters[y])
            
            res1 = res1 + letters[y]
            res2 = res2 + letters[z]
        print "Key (CT1)=", res1
        print "Key (CT2)=", res2

def FindPT(aWord):
    print "testing %s" % aWord
    thisWord = LettersNaarCijfers(aWord)      #omzetten naar cijfersequentie

    LoopTot = len(x) - len(thisWord) +1     #len(CT1) = len(CT2)=len(x)
    for i in range(0,LoopTot):
        res1 = ""  #PT

        for j in range(0,len(thisWord)):
            y = int(x[j+i]) ^ int(thisWord[j]) #XOR
            print "x[%d]=%s  Word[%d]=%s x=%s" % (j+i,x[j+i], j, thisWord[j], letters[y])
            res1 = res1 + letters[y]
            
        print "PT=", res1
        
    
                    
#geef aan wat in hoofdzaak moet gebeuren
def main():
    print "Crib Dragging the XOR-ed CT %s" % (x)

    global hits
    hits = []
    for crib in cribs:
        print "Controle op %s" % crib
        cribdrag(crib, x)           #zoek naar crib
    if len(hits)>0:                 #zijn er gevonden?
        print "Gevonden cribs zijn ", hits

    #FindKey("kill")
    FindPT("killhitler")
    

#als deze code geen module is, run het als main    
if __name__ == '__main__':
    main()



