#Senior Citizen

age = float(input("Enter the age: "))
    

if (age > 0 and age <= 1):
    print ("Infant")
elif (age > 1 and age <= 18):
    print ("Child")
elif (age > 18 and age <= 60):
    print ("Adult")
else:
    print ("Senior Citizen")