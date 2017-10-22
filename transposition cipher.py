print (" Enter the string to encrypted ")
plainText = input()

print(" Enter the key ")
key = input()

length = len(plainText)
print (length)
cipherText = ''

for x in range(len(plainText)):
    z = 0
    cipher = plainText[z]+ plainText[z + 10]
    z= z + 1
    cipherText = cipherText + cipher
    
print(cipherText)
