from datetime import datetime #importera metoden datetime från datetime

#Uppgift 0a
import lab0
lab0.temp()

#Uppgift 1a
name = input("Vad heter du: ") #Ta namn
print("Hej", name + '!')
age = input("Mata in din ålder: ") #Ta ålder
dob = datetime.now().year - int(age) #Ta nuvarande år och subtrahera ålder
print(dob)
county = input("Vilket län föddes du i: ")

#Ta en slice av namn från 0 till hälften
#Och sätt ihop med län från hälften till längd av län
print(f"{name[0:len(name)//2]}{county[len(county)//2:len(county)]}")
