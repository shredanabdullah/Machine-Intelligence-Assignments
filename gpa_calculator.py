from typing import List
from college import Student, Course
import utils

def calculate_gpa(student: Student, courses: List[Course]) -> float:
    '''
    This function takes a student and a list of course
    It should compute the GPA for the student
    The GPA is the sum(hours of course * grade in course) / sum(hours of course)
    The grades come in the form: 'A+', 'A' and so on.
    But you can convert the grades to points using a static method in the course class
    To know how to use the Student and Course classes, see the file "college.py"  
    '''
    #TODO: ADD YOUR CODE HERE
    student_courses = [course for course in courses if student.id in course.grades]
    ######this is what makes the the test case wrong
    '''
    - Student('1105', 'Ahmed')
    - [Course('CMPN402', 'MI', 3, {'1105':'A', '1203':'B'}), Course('CMPN205', 'CG', 2, {'1105':'B', '1203':'A'}), Course('CMPN666', 'AHS', 2, {'1203':'D'})]
    calculate the gpa based on the entered id 1105
    ''' 

    total_points = 0
    total_hours = 0

    for course in student_courses:
        # Get the grade for the student in the course, default to 'F' if not available
        student_grade = course.grades.get(student.id, "F")
        grade_point = Course.convert_grade_to_points(student_grade)
        
        total_points += course.hours * grade_point
        total_hours += course.hours

    if total_hours == 0:
        return 0.0  

    gpa = total_points / total_hours
    return gpa
    # total_points = 0
    # total_hours = 0

    # for course in courses:
    #     grade_point = Course.convert_grade_to_points(course.grades.get(student.id, "F"))
    #     total_points += course.hours * grade_point
    #     total_hours += course.hours

    # if total_hours == 0:
    #     return 0.0  

    # gpa = total_points / total_hours
    # return gpa