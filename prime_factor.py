n=320
i = 2
factor = []
while (n>1):
    if (n%i==0):
        factor.append(i)
        n=n/i
    else:
        i=i+1
print (factor)
