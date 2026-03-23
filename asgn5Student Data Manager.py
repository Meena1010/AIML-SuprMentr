students = {
    "A": 85,
    "B": 92,
    "C": 78,
    "D": 88,
    "E": 95
}

topper = max(students, key=students.get)
average = sum(students.values()) / len(students)

def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"

print("Topper:", topper, "-", students[topper])
print("Class Average:", average)

print("\nGrades:")
for name, marks in students.items():
    print(name, ":", get_grade(marks))