

f=open(r'C:\Temp\kleineFile.txt','r')
wordList = []
lijn = f.readline()

if len(lijn)>0:
        print "Voor",lijn
        temp = lijn.strip('\"\n., ')
        
        print temp

       


##while lijn:
##    print lijn, 
##    lijn = f.readline()
##    if len(lijn)>0:
##        temp = lijn.split(' ')
##
##        for woord in temp:
##            print woord
    

f.close()


