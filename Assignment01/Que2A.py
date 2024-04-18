num = int(input("Enter the number : "))

print(f"The entered number is {num}")

d = num%10
num = num/10

c = num%10
num = num/10

b = num%10
num = num/10

a = num

print(f"Face value of each decimal :- {int(a)}  {int(b)}  {int(c)}  {int(d)}")

    
    
