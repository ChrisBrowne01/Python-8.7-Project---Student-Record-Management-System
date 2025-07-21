#Project: Student Record Management System

# 1. Create tuples to store student information (name, age, grade).
student_1 = ("Christina", 31, "a")
student_2 = ("Bobby", 28, "C")
student_3 = ("Danniel", 24, "B")
student_4 = ("Alice", 30, "A")
student_5 = ("John", 22, "B")

students = (student_1, student_2, student_3, student_4)
# 2. Use tuple methods to count and index elements.
grade_count = students.count("B")
print(f"Number of students: {len(students)}")
print(f"Index of Jane Smith: {students.index(student_2)}")

# 3. Create sets to store unique student IDs and courses.
student_ids = {1002, 1003, 1004, 1005, 1006, 1007}
student_courses = {"Web Programming", "Social Media", "Web Programming", "English", "Web Programming"}

# 4. Perform set operations like union, intersection, and difference.
print(f"Student IDs: {student_ids}")
print(f"Courses: {student_courses}")

new_students = {1006, 1007}
student_ids.update(new_students)
print(f"Updated Student IDs: {student_ids}")

completed_courses = {"Social Media", "English"}
# Perform set operations
all_courses = student_courses.union(completed_courses)
print(f"All Courses: {all_courses}")
remaining_courses = student_courses.difference(completed_courses)
print(f"Remaining Courses: {remaining_courses}")

# Use frozen sets to create immutable sets of student data.
frozen_courses = frozenset(["Math", "Social Media", "English"])
print(f"Frozen Courses: {frozen_courses}")

# Attempt to modify a frozen set (will raise an error)
# frozen_courses.add("Art")
# Uncommenting this line will raise an AttributeError

# Create a frozen set of student data
frozen_student_data = frozenset(students)
print(f"Frozen Student Data: {frozen_student_data}")