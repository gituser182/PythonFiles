import os

print os.getcwd()
woorden = []

#Lees een file (1 woord per lijn) - stop in list
f = open('/Users/Dany/Desktop/PythonFiles/FullWordList.txt','r')
for line in f:
    woorden.append(line.strip('\r\n'))
f.close()
print woorden

#mystr = "Nu nog, een test op, komma's en dergerlijke! he likes ike kill hilter".lower()
#li = mystr.split()
#print li

goed = 'abcdefghijklmnopqrstuvwxyz'
letterset = 'kilhtres'


#goedgekeurd = []
#aanvaard = []
#for woord in li:
    #for letter in woord:
        #if letter in goed:
            #pass
        #else:
            #print letter,woord
            #woord= woord.replace(letter,'')
            
    #if woord not in goedgekeurd:
        #goedgekeurd.append(woord)
        
#print""
#print "lijst met éénmalig voorkomende woorden"
#print goedgekeurd  

aanvaard = []
for woord in woorden:
    IsGoedgekeurd = True
    for letter in woord:
        if not letter in letterset:
            IsGoedgekeurd = False
            
    if IsGoedgekeurd:
        aanvaard.append(woord)
        
print "De volgende %d woorden bevatten de juiste letterset" % len(woorden)
print aanvaard


            
    