# Ask for number of students and subjects
num_students = int(input("Enter number of students: "))
num_subjects = int(input("Enter number of subjects: "))

total_class_average = 0  # To accumulate all students' averages

for student in range(1, num_students + 1):
    print(f"\nStudent {student}")
    total_score = 0

    # Input scores for each subject
    for subject in range(1, num_subjects + 1):
        score = float(input(f"Enter score {subject}: "))
        total_score += score

    # Compute and display student average
    student_average = total_score / num_subjects
    print(f"Average for Student {student} = {student_average:.1f}")

    # Add to class total
    total_class_average += student_average

# Compute overall class average
class_average = total_class_average / num_students
print(f"\nClass Average = {class_average:.1f}")
