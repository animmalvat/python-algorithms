#this is a simple program that finds gcd using euclids alogirthm

#function returns the gcd of two given numbers
def gcd(a, b):
    r = 0 # this is the remainder
    while(a % b !=0): 
        r = a % b 
        a = b;
        b = r;
    return b
