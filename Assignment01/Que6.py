num = int(input("Enter the number : "))

def Factorial(num):
    temp = 1
    i = 1
    while i <= num:
        temp*=i
        i=i+1
    return temp

print(f"{Factorial(num)}")
    