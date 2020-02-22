#recursion function to calculate power of number
def power(num, pwr):
    if pwr == 0:
        return 1
    else: 
        return num * power(num, pwr - 1);
    
temp = power(2, 3)
print(temp);