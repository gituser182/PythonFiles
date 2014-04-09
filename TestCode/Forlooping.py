print ('Test Python 3 - For loop en While loop')


myname = input('Geef uw naam:')
print('Howdy, ' + myname + '\n')

spam = 'azertyuiop'

print('\ngewone range...')
for a in range(0,10): #fixed to a specidic number
    print (a, spam[a])

print ('\ngebruike van len()')
for a in range(len(spam)): #how it should be
    print (a, spam[a])

print('\ngebruik van len() en -1')
for a in range(len(spam)-1 ,-1, -1):
    print (a, spam[a]) #achterstevoren met for

print('\nGebruik van een while loop...')
i = len(spam) - 1 # -1 nul-based
translation = '';
while (i>=0):
    translation = translation + spam[i]
    print (spam[i])
    i = i - 1
print ('Omgekeerd: ' + translation)
  

print ('\neinde test')
