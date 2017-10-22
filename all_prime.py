
def is_prime(num):
    k=0
    for i in range(2,int(num/2)):
        if (num%i==0):
            return False
        else:
            return True



def main():
    print ("Enter a Number")
    num = input()
    for i in range (2,int(num)):
        if(is_prime(i) is True):
            print(i)



if __name__ == '__main__':
    main()
