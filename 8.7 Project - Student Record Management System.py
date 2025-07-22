#Project: Student Record Management System

# 1. Create Tuples to store student information (name, age, grade).
student_1 = ("Christina Bow", 31, "A")
student_2 = ("Bobby Dane", 28, "C")
student_3 = ("Danniel Baker", 24, "B")
student_4 = ("Alice Longstaff", 30, "A")
student_5 = ("John Smith", 22, "B") 

# Create a Tuple of students
students = (student_1, student_2, student_3, student_4, student_5)

# 2. Use Tuple methods to count and index elements.
print(f"Number of students: {len(students)}")
print(f"Index of Bobby Dane: {students.index(student_2)}")

# 3. Create Sets to store unique student IDs and courses.
student_ids = {1002, 1003, 1004, 1005, 1006, 1007}
student_courses = {"Web Programming", "Social Media", "Web Programming", "English", "Web Programming"}

# 4. Perform set operations like union, intersection, and difference.
print(f"Student IDs: {student_ids}")
print(f"Courses: {student_courses}")

new_students_ids = {1008, 1009} 
student_ids.update(new_students_ids)
print(f"Updated Student IDs (added 1008, 1009): {student_ids}")

# Perform set operations
completed_courses = {"Social Media", "English"}
all_courses = student_courses.union(completed_courses)
print(f"All Courses (union): {all_courses}")

remaining_courses = student_courses.difference(completed_courses)
print(f"Remaining Courses (difference): {remaining_courses}")

common_courses = student_courses.intersection(completed_courses)
print(f"Common Courses (intersection): {common_courses}")

# 5. Use frozen sets to create immutable sets of student data.
frozen_courses = frozenset(["Math", "Social Media", "English"])
print(f"Frozen Courses: {frozen_courses}")

# Attempt to modify a frozen set (will raise an error)
# frozen_courses.add("Art")
# Uncommenting this line will raise an AttributeError

# Create a frozen set of student data
frozen_student_data = frozenset(students)
print(f"Frozen Student Data: {frozen_student_data}")