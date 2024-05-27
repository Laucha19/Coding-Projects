def find_average_marks(marks):
    sum_of_marks  = sum(marks)
    total_subjects = len(marks)
    average_of_marks = sum_of_marks / total_subjects
    return average_of_marks

def grade_marks(average_of_marks):
    if average_of_marks >= 90:
        grade = 'A'
    elif average_of_marks >= 80:
        grade = 'B'
    elif average_of_marks >= 70:
        grade = "C"
    elif average_of_marks >= 60:
        grade = 'D'
    else:
        grade = "F"
    return grade


marks = [55, 65, 75, 85, 95]
average_of_marks = find_average_marks(marks)
print("This is your average grade:", average_of_marks)

grade = grade_marks(average_of_marks)
print("Your final grade for the class is:", grade)





