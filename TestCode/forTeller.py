#for loop
som = 0
numbers = [1,3,5,7,9]
for teller in numbers:
    som = som + teller
    print teller
print 'som = %d' % som


zin = "Dit is een test" #5 klinkers

#door een string lopen
teller = 0
for l in zin:
    if l in ['a','e','i','u','o','y']:
        teller = teller +1
print "%d klinkers in zin van lengte %d" %(teller, len(zin))


#hetzelfde, maar via een index
teller = 0
for l in range(0,len(zin)):
     if zin[l] in ['a','e','i','u','o','y']:
        teller = teller +1
print "%d klinkers in zin van lengte %d" %(teller, len(zin))

nummers = [1,2,3,4,5,6,7,8,9,10]

for nummer in range(0,len(nummers),2): #step per twee
    print nummer

#via tuples
print "\n"    
getallen=(1,2,3,4,5)
for g in getallen:
    print g


# berekenen van faculteiten
f= int(raw_input('Geef een getal: '))    
fact = 1
for i in range(1, f +1):  #+1 nodig om voledige lijst te hebben
    fact = fact * i
print "factorial van %d is %d " % ( f, fact)    

        
