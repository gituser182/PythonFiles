"""
Opgave: Genereren van de dictionary

Gegeven: binair met 8 letters
    0) 000 = e
    1) 001 = h
    2) 010 = i
    3) 011 = k
    4) 100 = l
    5) 101 = r
    6) 110 = s
    7) 111 = t

Als het resultaat van een XOR gelijk is aan 000,
welke twee getallen moet men dan XOR'en om dit resultaat te bekomen?
0 = 0 XOR 0, 1 XOR 1, ...

Als het resultaat van een XOR gelijk is aan 001, welk zijn dan die getallen?
1 = 0 XOR 1, 1 XOR 0, ...

Zo ook voor de getallen 2,3,4,5,6 en 7

Maar hier vervolgens een dictionary van in de vorm
dict[0] = [ [letters[0],letters[0]],   # 0 XOR 0
            [letters[1],letters[1]],   # 1 XOR 1
            [letters[2],letters[2]],
            [letters[3],letters[3]],
            [letters[4],letters[4]],
            [letters[5],letters[5]],
            [letters[6],letters[6]],
            [letters[7],letters[7]]
          ]
De output hiervan wordt verder gebruikt in dictOefening          
"""
letters = ['e', 'h', 'i', 'k', 'l', 'r', 's', 't']

for i in range (0,8):
    #print "maken van dict[%d] " % i
    strRes = "dict[%d] = [ " %i
    for j in range (0,8):
        res = i ^ j
        #print bin(i), " = ",  bin(j), " XOR ", bin(res)
        strRes = strRes + "[letters[%d],letters[%d]]" %(j,res)
        if j == 0:
            strRes = strRes + ','  # eerste "," plaatsen
        if j % 7 != 0:
            strRes = strRes + ','  # allerlaatste heeft geen "," nodig
        strRes = strRes + "     # %s = %s XOR %s\n" %(bin(i),bin(j),bin(res))     
           
    strRes = strRes + ' ]'
    print strRes

"""
Resultaat:

dict[0] = [ [letters[0],letters[0]],     # 0b0 = 0b0 XOR 0b0
[letters[1],letters[1]],     # 0b0 = 0b1 XOR 0b1
[letters[2],letters[2]],     # 0b0 = 0b10 XOR 0b10
[letters[3],letters[3]],     # 0b0 = 0b11 XOR 0b11
[letters[4],letters[4]],     # 0b0 = 0b100 XOR 0b100
[letters[5],letters[5]],     # 0b0 = 0b101 XOR 0b101
[letters[6],letters[6]],     # 0b0 = 0b110 XOR 0b110
[letters[7],letters[7]]     # 0b0 = 0b111 XOR 0b111
 ]
dict[1] = [ [letters[0],letters[1]],     # 0b1 = 0b0 XOR 0b1
[letters[1],letters[0]],     # 0b1 = 0b1 XOR 0b0
[letters[2],letters[3]],     # 0b1 = 0b10 XOR 0b11
[letters[3],letters[2]],     # 0b1 = 0b11 XOR 0b10
[letters[4],letters[5]],     # 0b1 = 0b100 XOR 0b101
[letters[5],letters[4]],     # 0b1 = 0b101 XOR 0b100
[letters[6],letters[7]],     # 0b1 = 0b110 XOR 0b111
[letters[7],letters[6]]     # 0b1 = 0b111 XOR 0b110
 ]
dict[2] = [ [letters[0],letters[2]],     # 0b10 = 0b0 XOR 0b10
[letters[1],letters[3]],     # 0b10 = 0b1 XOR 0b11
[letters[2],letters[0]],     # 0b10 = 0b10 XOR 0b0
[letters[3],letters[1]],     # 0b10 = 0b11 XOR 0b1
[letters[4],letters[6]],     # 0b10 = 0b100 XOR 0b110
[letters[5],letters[7]],     # 0b10 = 0b101 XOR 0b111
[letters[6],letters[4]],     # 0b10 = 0b110 XOR 0b100
[letters[7],letters[5]]     # 0b10 = 0b111 XOR 0b101
 ]
dict[3] = [ [letters[0],letters[3]],     # 0b11 = 0b0 XOR 0b11
[letters[1],letters[2]],     # 0b11 = 0b1 XOR 0b10
[letters[2],letters[1]],     # 0b11 = 0b10 XOR 0b1
[letters[3],letters[0]],     # 0b11 = 0b11 XOR 0b0
[letters[4],letters[7]],     # 0b11 = 0b100 XOR 0b111
[letters[5],letters[6]],     # 0b11 = 0b101 XOR 0b110
[letters[6],letters[5]],     # 0b11 = 0b110 XOR 0b101
[letters[7],letters[4]]     # 0b11 = 0b111 XOR 0b100
 ]
dict[4] = [ [letters[0],letters[4]],     # 0b100 = 0b0 XOR 0b100
[letters[1],letters[5]],     # 0b100 = 0b1 XOR 0b101
[letters[2],letters[6]],     # 0b100 = 0b10 XOR 0b110
[letters[3],letters[7]],     # 0b100 = 0b11 XOR 0b111
[letters[4],letters[0]],     # 0b100 = 0b100 XOR 0b0
[letters[5],letters[1]],     # 0b100 = 0b101 XOR 0b1
[letters[6],letters[2]],     # 0b100 = 0b110 XOR 0b10
[letters[7],letters[3]]     # 0b100 = 0b111 XOR 0b11
 ]
dict[5] = [ [letters[0],letters[5]],     # 0b101 = 0b0 XOR 0b101
[letters[1],letters[4]],     # 0b101 = 0b1 XOR 0b100
[letters[2],letters[7]],     # 0b101 = 0b10 XOR 0b111
[letters[3],letters[6]],     # 0b101 = 0b11 XOR 0b110
[letters[4],letters[1]],     # 0b101 = 0b100 XOR 0b1
[letters[5],letters[0]],     # 0b101 = 0b101 XOR 0b0
[letters[6],letters[3]],     # 0b101 = 0b110 XOR 0b11
[letters[7],letters[2]]     # 0b101 = 0b111 XOR 0b10
 ]
dict[6] = [ [letters[0],letters[6]],     # 0b110 = 0b0 XOR 0b110
[letters[1],letters[7]],     # 0b110 = 0b1 XOR 0b111
[letters[2],letters[4]],     # 0b110 = 0b10 XOR 0b100
[letters[3],letters[5]],     # 0b110 = 0b11 XOR 0b101
[letters[4],letters[2]],     # 0b110 = 0b100 XOR 0b10
[letters[5],letters[3]],     # 0b110 = 0b101 XOR 0b11
[letters[6],letters[0]],     # 0b110 = 0b110 XOR 0b0
[letters[7],letters[1]]     # 0b110 = 0b111 XOR 0b1
 ]
dict[7] = [ [letters[0],letters[7]],     # 0b111 = 0b0 XOR 0b111
[letters[1],letters[6]],     # 0b111 = 0b1 XOR 0b110
[letters[2],letters[5]],     # 0b111 = 0b10 XOR 0b101
[letters[3],letters[4]],     # 0b111 = 0b11 XOR 0b100
[letters[4],letters[3]],     # 0b111 = 0b100 XOR 0b11
[letters[5],letters[2]],     # 0b111 = 0b101 XOR 0b10
[letters[6],letters[1]],     # 0b111 = 0b110 XOR 0b1
[letters[7],letters[0]]     # 0b111 = 0b111 XOR 0b0
 ]
"""
    
        
