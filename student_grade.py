here# Simple Student Grade Calculator

# Taking input marks for 5 subjects
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))
sub5 = float(input("Enter marks for Subject 5: "))

# Calculating total and average
total = sub1 + sub2 + sub3 + sub4 + sub5
average = total / 5

# Calculating grade
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Display results
print("\nTotal Marks:", total)
print("Average:", average)
print("Grade:", grade)
