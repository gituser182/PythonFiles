import os

print os.getcwd()
woorden = []
aanvaard = []
goed = 'abcdefghijklmnopqrstuvwxyz'
letterset = 'kilhtres'

#Lees een file (1 woord per lijn) - stop in list
f = open('/Users/Dany/Desktop/PythonFiles/FullWordListJaneEyre.txt','r')
for line in f:
    woorden.append(line.strip('\r\n'))  #verwijder '\r\n' in elke regel
print "%d aantal woorden" % len(woorden)


for woord in woorden:
    IsGoedgekeurd = True
    for letter in woord:
        if not letter in letterset:
            IsGoedgekeurd = False
            
    if IsGoedgekeurd:
        aanvaard.append(woord)
        
print "De volgende %d woorden bevatten de juiste letterset:" % len(aanvaard)
print aanvaard


            
    