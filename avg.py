def calculate_grade(m1, m2, m3, m4, m5):
    """Takes marks of 5 subjects, returns average and grade."""
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

def get_mark(subject_num):
    """Reads and validates a single subject mark."""
    while True:
        try:
            mark = float(input(f"Enter marks for subject {subject_num}: "))
            if mark < 0 or mark > 100:
                print("Please enter a value between 0 and 100.")
            else:
                return mark
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Main program
sub1 = get_mark(1)
sub2 = get_mark(2)
sub3 = get_mark(3)
sub4 = get_mark(4)
sub5 = get_mark(5)

avg, grd = calculate_grade(sub1, sub2, sub3, sub4, sub5)

print(f"\nAverage marks = {avg:.2f}")
print(f"Your grade is: {grd}")
