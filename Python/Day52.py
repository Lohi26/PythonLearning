# Input a Python list of student heights
student_heights = input().split(" ")
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
sum=0
for i in student_heights:
  sum+=i
print(sum//len(student_heights))