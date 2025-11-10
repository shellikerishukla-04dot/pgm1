def calculate_grade(m1, m2, m3, m4, m5):
   
    total = m1 + m2 + m3 + m4 + m5
    average = total / 5
    
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    return average, grade


sub1 = float(input("Enter marks for subject 1: "))
sub2 = float(input("Enter marks for subject 2: "))
sub3 = float(input("Enter marks for subject 3: "))
sub4 = float(input("Enter marks for subject 4: "))
sub5 = float(input("Enter marks for subject 5: "))


avg, grd = calculate_grade(sub1, sub2, sub3, sub4, sub5)


print(f"\nAverage marks = {avg:.2f}")
print(f"Your grade is: {grd}")
