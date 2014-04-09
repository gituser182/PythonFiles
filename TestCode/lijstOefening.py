#KNR 28/02/14
def OntleedLijn(aList):
    """
    Neem een tekstlijn (in vorm van een list) en controleer of
    er enkel letters instaan dewelke aanvaard zijn.
    Niet aanvaarde tekens (zoals komma, punt, ..) worden weggegooid
    """
    goed = 'abcdefghijklmnopqrstuvwxyz'  #aangenomen char
    for woord in aList:                  #voor elk woord in de lijst
        for letter in woord:             #ctrl elke letter per woord
            if letter in goed:
                pass
            else:                        #letter is niet aanvaard
                woord= woord.replace(letter,'') #onnodige tekens droppen
        #zeker zijn dat het een woord is dat niet is opgenomen in de lijst
        if woord not in goedgekeurd and len(woord)>0:
            goedgekeurd.append(woord)


def main():
    #definieren van globale var
    global goedgekeurd
    goedgekeurd = []

    deFile = 'c:\Temp\pandp.txt'
    deFile = '/Users/Dany/Desktop/PythonFiles/JaneEyre.txt'
    #inlezen van de file
    f = open(deFile,'r')                #open bestand 
    mystr = f.readline().lower()        #inlezen per lijn in lowercase
    while mystr:
        print mystr
        if len(mystr)>0:                #moet bewerkbaar zijn
            li = mystr.split()          #verwijder overtollige spaties
            OntleedLijn(li)             #verdere controle
        mystr = f.readline().lower()    #lees de volgende lijn uit de file
    f.close()

    #alfabetische volgorde afdwingen
    goedgekeurd.sort()

    #wegschrijven naar file
    f = open('/Users/Dany/Desktop/PythonFiles/FullWordListJaneEyre.txt','w')
    for woord in goedgekeurd:
        f.write(woord + '\n')
    f.close()
    print "Aantal unieke woordjes = %d" %len(goedgekeurd)
    print "Einde verwerking"

#Als dit niet in een module is, run deze code
if __name__ == "__main__":
    main()
