num = int(input("Enter the number : "))
rev = 0
print(f"The entered number is {num}")

while num != 0:
     rem = int(num % 10)
     rev = int(rev * 10 + rem)
     num = int(num / 10)

print(f"The reversed number is {int(rev)}")