#definieer een f(x)

def factor(n):                  #Eenvoudige manier (d is dikwijls paar)
    """
Eenvoudige manier van factorisatie 18/02/2014
    """ 
    d = 2                       #start met delen door 2
    factoren = []               #zet een lege list op
    while n>1:                  #zet loop op
        if n % d == 0:          #is de rest van de deling door d gelijk aan 0
            factoren.append(d)  #toevoegen aan list
            n = n/d             #deel getal door d
        else:                   #deling door d had nog een restwaarde
            d = d + 1           #probeer volgend getal in de rij
    return factoren


#definieer de main() steeds als voorlaatste "def"
def main():
    print factor.__doc__
    print "Factoriseren van 12345678987654321 geeft: ",  # "," = geen CRLF
    FactorGetallen = factor (12345678987654321)
    print FactorGetallen
    print "einde factor"

#Altijd helemaal onderaan de call naar main()
if __name__ == '__main__':
    main()    
