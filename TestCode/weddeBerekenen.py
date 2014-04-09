ratio=25.00
uurloon = 15.0
while True:
    
   print 'aantal werkuren: (-1 om te eindigen) ',
   urengewerkt = int(raw_input())
   if urengewerkt==-1:
       break  #einde 

   if urengewerkt >40:
      tebetalen = (urengewerkt*ratio/100 + urengewerkt) * uurloon
   elif urengewerkt <=40:
      tebetalen = urengewerkt * uurloon
   print'Uit te betalen = %.2f Euro' %tebetalen
   
raw_input('druk op enter')
