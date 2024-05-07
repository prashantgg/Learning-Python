marks1 = int(input("Enter marks of Science:"))
marks2 = int(input("Enter marks of Maths:"))
marks3 = int(input("Enter marks of Social:"))
totPass = (marks1+marks2+marks3)/3
if (marks1>33 and marks2>33 and marks3>33 and totPass>=40):
    print ("Student is pass")
else:
    print ("Student in fail")

