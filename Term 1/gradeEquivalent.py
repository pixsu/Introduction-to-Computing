print("National University Grading System")
grade = int(input("Enter your grade: "))

if grade <= 100 and grade >= 96:
    print("Your grade is 4.0")   
elif grade <= 95 and grade >= 90:
    print ("Your grade is 3.5")
elif grade <= 89 and grade >= 84:
    print ("Your grade is 3.0")
elif grade <= 83 and grade >= 78:
    print ("Your grade is 2.5")
elif grade <= 77 and grade >= 72:
    print ("Your grade is 2.0")
elif grade <= 71 and grade >= 66:
    print ("Your grade is 1.5")
elif grade <= 65 and grade >= 60:
    print ("Your grade is 1.0")
elif grade <= 59:
    print ("0.0")
else:
    print ("GRADE UNIDENTIFIED")
