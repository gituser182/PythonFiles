#een loop
print "schrijf punten naar file\n"
som = 0.0     #nodig om gemiddelde te berekenen
teller = 0  #nodig om gemiddelde te berekenen

f = open('punten.txt', 'w') #open voor write

print "Voer punten in ('q' om te stoppen)",  #, om einde om input op 
punten = raw_input()                         # dezelfde regel te hebben
punten = punten.upper()
while (punten != 'Q'):
   
    if punten.isdigit():          #zeker zijn dat het digits zijn
        som = som + float(punten) #omzetten naar float
        teller = teller + 1       #bijhouden van het aantal geldige inputs
        f.write(punten +'\n')    #schrijf naar file

    print "Voer punten in ('q' om te stoppen)",
    punten = raw_input()
    punten = punten.upper()    

if teller>0:
    #print teller, som
    print "gemiddelde punten zijn %.2f voor %d gegevens" %(float(som/teller), teller)
else:
    #print teller, som 
    print "Er zijn geen gegevens ingeschreven"

f.close() #pas bij deze bewerking wordt de interne buffer naar schijf gedumpt


##### Opnieuw openen en uitlezen
#####

f = open('punten.txt','r')

punten = f.readline()
while punten:
    print punten.split('\n')[0] #haal de \n eruit via split
                                #dit komt in een list terecht, geef daaruit 0e element
    punten = f.readline()
f.close()
