#!/usr/bin/env python3

def func(param):
    #param is een local var = copy van oorspronkelijke waarde
    #immutables (zoals strings, getallen) blijven onveranderd
    #mutables (zoals lists) kunnen aangepast worden
    print ('tijdens func param = %s' %param)
    param = param + '42'
    print ('aangepast tijdens func param = %s' %param)
    return (param) #doorgeven van een veranderde waarde

def NoCrash():
    global spam  #nu praat men over global var
    spam = 'Ola' #waaraan men wel een andere waarde mag toekennen
    print('NoCrash waarde = %s' %spam)

def crash():
    print(spam) #dit drukt de globale var af
    #spam = 2   #OPGELET: men mag in een f(x)
                #een global var geen andere waarde toekennen
 
print('Demo van een param door te geven aan een f(x)\n')    
spam = 'hello'  #Dit is de global var
print ('(voor func) spam = %s' %spam)

returnwaarde = func(spam)

print ('(na func) spam = %s' %spam)
print ('(na func) returnwaarde = %s' %returnwaarde)

print('\nOproepen Crash en Crash2')
NoCrash()
crash()
print ('Done...')