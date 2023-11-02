# Class exercise #2 (DICTIONARIES)

grades = {'course': 'Intro to Programming', 'instructor': 'Dr Albert Einstein', 'Allen': 90,
          'Barbara': 92, 'Charles': 80, 'Denise': 85, 'Edward': 74, 'Frances': 80, 'Gary': 60, 'Harry': 94,
          'Janice': 91, 'Kelly': 84, 'Larry': 87}


# Adding
def add_grades(name, grade):
    grades[name] = grade


add_grades('Mary', 100)
add_grades('Nancy', 64)
add_grades('Olivia', 88)


# 1.
def get_name_and_grades():
    """
    Gets student names and grades from the variable 'grades'. removes course name and instructor

    :return: student list, grade list
    """
    student_list = []
    grades_list = []
    grades.pop('course')
    grades.pop('instructor')
    for name in grades:
        student_list.append(name)
        grades_list.append(grades[name])
    return student_list, grades_list


student_names, student_grades = get_name_and_grades()
# print(student_names)
# print(student_grades)

print("Class Statistics")
print("-----------------------")
# 2.
num_students = len(student_names)
print('There are', num_students, 'student(s)')


# 3.
def low_avg_high(numerical_list):
    """
    Gets the lowest, highest, and average value for a given list
    :param numerical_list:  to determine low, high and avg from. Must be a list of integers
    :return: lowest value, highest value, and average value
    """
    sorted_list = numerical_list
    sorted_list.sort()

    list_length = len(sorted_list)
    low = sorted_list[0]
    high = sorted_list[-1]
    total = 0
    for num in sorted_list:
        total += num
    avg = total / list_length

    return low, high, avg


low_grade, high_grade, avg_grade = low_avg_high(student_grades)
print("The lowest grade is a", low_grade, "\nThe average grade is a", avg_grade, "\nThe highest grade is a",
      high_grade)

# 4.
grades_sorted = {}
for i in range(len(student_grades)):
    grades_sorted[student_grades[i]] = student_names[i]

grades_sorted = dict(sorted(grades_sorted.items(), reverse=True))

# 5.
print("-----------------------")
print("The student's grades as strings")
print("-----------------------")
for grade, name in grades_sorted.items():
    print(name, "has a grade of", grade)
print("-----------------------")
# 6. & 7.
print("Ranking")
print("-----------------------")
print("Rank | Name | Grade")
rank = 1
for grade, name in grades_sorted.items():
    if rank < 10: # Fixes spacing issue
        print(rank, "   |", name, "|", grade)
    else:
        print(rank, "  |", name, "|", grade)
    rank += 1
