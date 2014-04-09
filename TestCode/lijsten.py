#!/usr/bin/env python3

print('Oefeningen op lists\n')

mijnlijst = ['1','2','3','4']
print (mijnlijst[0], ',', mijnlijst[3])


mijn2eLijst = ['x'] *4  
print(mijn2eLijst)           #geeft 4 keer een enkele x
print (''.join(mijn2eLijst)) #geeft xxxx aan elkaar


idemlijst = list(range(4))
print (idemlijst) #0,1,2,3


mylist = list('Hello world!') #h,e,l,l,o, ,w,o,r,l,d,!
print (mylist)

#vervang de 'o' en de '!' door een 'a' in mylist
for symbol in mylist:
    if (symbol == 'o') or (symbol=='!'):
       num = mylist.index(symbol) #bepaal de index(num) waar een 'o' staat
       #print(num)
       mylist.remove(symbol)  #neem de inhoud op deze plaats weg
       mylist.insert(num,'a') #zet een 'a' in de plaats
       
print('Aangepast = %s' %mylist)       
       




