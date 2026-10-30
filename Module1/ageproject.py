#this project is based of of voting eligibility and licence
age = int(input("Enter your age\n"))
if age >=10 and age <=20 :
    print("you are old enough  to vote")
else:
    print("you are too young to vote")

drive = input("enter year you got driver license.If never,type no\n")

if drive == "no": 
    print("too young to drive")
    
else:
    print("old enough to drive")

   