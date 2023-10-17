# the program to display 'unrecognized marks/avg' if a negative
# value or a value greater than 100 is keyed in
def calculate_grade():
    subjects = ["Maths", "Physics", "Geo", "Chem"]
    marks = []

    for subject in subjects:
        try:
            mark = float(input(f"Enter {subject} marks (0-100): "))
            if mark < 0 or mark > 100:
                print("Unrecognized marks/avg")
                return
            marks.append(mark)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return

    average = sum(marks) / len(marks)

    if 0 <= average <= 30:
        grade = 'D'
    elif 31 <= average <= 50:
        grade = 'C'
    elif 51 <= average <= 70:
        grade = 'B'
    elif 71 <= average <= 100:
        grade = 'A'
    else:
        print("Unrecognized marks/avg")
        return

    print(f"Average marks: {average}")
    print(f"Grade: {grade}")

calculate_grade()
