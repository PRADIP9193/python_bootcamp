#For loop with Python Lists 
# fruits=["Apple","Peach","Pear","Cherry","Tomato"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Soop")
# print(fruits)

# Exercise of for loop

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
print(student_heights)

# total_height = sum(student_heights)
total_height = 0
for height in student_heights:
    total_height= total_height + height
# print(total_height)

# number_of_students = len(student_heights)
number_of_students = 0
for student in student_heights:
    number_of_students = number_of_students + 1
# print(number_of_students)
average_height = round(total_height / number_of_students)
print(average_height)

