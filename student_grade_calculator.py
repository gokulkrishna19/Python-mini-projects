

def calculate_grade(average):
    """Return grade based on average marks."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

def main():
    print("=== Student Grade Calculator ===")

    name = input("Enter student name: ")
    subjects = int(input("Enter number of subjects: "))

    total = 0
    for i in range(subjects):
        mark = float(input(f"Enter mark for subject {i+1}: "))
        total += mark

    average = total / subjects
    grade = calculate_grade(average)

    print("\n📘 Student Report")
    print(f"Name     : {name}")
    print(f"Average  : {average:.2f}")
    print(f"Grade    : {grade}")

if __name__ == "__main__":
    main()
