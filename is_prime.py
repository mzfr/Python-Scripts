num= 4
k=0
for i in range(2,int(num/2)):
    if (num%i==0):
        k = k+1

if (k==0):
    print("IS a prime number")
else:
    print("IS not a prime number")
