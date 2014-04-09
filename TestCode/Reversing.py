#test reverse
print ('...Inversing a string...')
message = input('Typ een bericht:')
translated = ''

i = len(message) - 1  #-1: telt vanaf nul!  Eerste element staat op message[0]
print('lengte bericht = ', len(message))
while i >=0:
    print ('bericht[', i ,']', message[i])
    translated = translated + message[i]
    i = i-1
    print ('nieuwe waarde van i=',i)

print (message, ' achterstevoren = ',translated)
