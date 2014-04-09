cipher1 = '20d916c6c29ee53c30ea1effc63b1c72147eb86b998a25c0cf1bf66939e8621b3132d83abb1683df619238'  
cipher2 = '20d916c6c29ee54343e81ff1b14c1372650cbf19998f51b5c51bf66f49ec62184034a94fc9198fa9179849'  
plaintext1 = 'zone-4-F7677DA8-3D77-11E2-BB65-E4BF6188709B'  
plaintext2 = ''  
key = []  
for i in range(0,len(cipher1),2):  
    key.append(int(cipher1[i:i+2],16) ^ int(cipher2[i:i+2],16))  
 
for i in range(0,len(plaintext1)):  
    plaintext2 = plaintext2 + chr(ord(plaintext1[i]) ^ key[i])  

plaintext2  
# 'zone-4-9D469367-B60E-4E08-BDF1-FED7CC74AF33'  
