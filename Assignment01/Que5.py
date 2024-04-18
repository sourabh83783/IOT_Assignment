n1 = int(input("Enter the first Sub marks : "))

n2 = int(input("Enter the second Sub marks : "))

n3 = int(input("Enter the third Third Sub marks : "))

Average = int((n1 + n2 + n3) / 3)

if (Average >= 90 and Average <=100):
    print(f"The average of student mark is {Average} and he got A Garde")

elif (Average >= 80 and Average <=89):
    print(f"The average of student mark is {Average} and he got B Garde")

elif (Average >= 70 and Average <= 79):
    print(f"The average of student mark is {Average} and he got C Garde")

elif (Average >= 60 and Average <=69):
    print(f"The average of student mark is {Average} and he got D Garde")

else:
    print(f"The average of student mark is {Average} and he got F Garde")