print "zoek mogelijkheden die het resultaat van 5 ^7 kunnen vormen" 
teller = 0
for i in range(8):
    for j in range(8):
        if i ^j == 5 ^ 7:
            print "%d^%d = %s ^%s " %(i,j, bin(i), bin(j))
            teller = teller + 1

print "Er zijn %d combinaties" % teller            
            
