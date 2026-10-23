def validate_mark(mark):
    if not 0 <= mark <= 100:
        raise ValueError("Marks must be between 0 and 100.")
    return mark


def calculate_total(marks):
    return sum(marks)


def calculate_average(total, number_of_subjects):
    return total / number_of_subjects


def assign_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def analyze_student(name, marks):
    total = calculate_total(marks)
    average = calculate_average(total, len(marks))
    grade = assign_grade(average)

    print(f"\nStudent Name: {name}")
    print(f"Marks: {marks}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Grade: {grade}")


def main():
    students = []

    for i in range(1, 4):
        name = input(f"Enter student {i} name: ").strip()
        marks = []

        for subject in ("Math", "Science", "English"):
            while True:
                try:
                    mark = float(input(f"Enter {name}'s marks in {subject}: "))
                    validated_mark = validate_mark(mark)
                    marks.append(validated_mark)
                    break
                except ValueError as error:
                    print(error)
                    print("Please enter a valid mark between 0 and 100.")

        students.append((name, marks))

    for name, marks in students:
        analyze_student(name, marks)


if __name__ == "__main__":
    main()
