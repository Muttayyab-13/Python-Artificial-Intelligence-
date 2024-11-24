import math 

# QUESTION 1
# a
name=input("Enter your name :")

age=int(input("Enter your age :"))

student=True
print(name)
print(age)
print(student)
#b

print(age+25)
print(name+" Smith")
student=False
print(student)

#Question 2:
# A
width=25.5
height=3.25

area=width*height

print(area)

#b
temp_cel = float(input("Enter temperature in Celsius: "))

print(f"The entered temperature is {temp_cel} C")

temp_Far=int(temp_cel * 9/5) + 32 

print(f"The temperature in faurenheit is {temp_Far} F")



"""c)Take radius of the circle as input from user. Calculate the area of a circle with this radius and store it in a variable called area. Print area at the end of your code. 
(Use the formula: area = π * radius^2, where π (pi) is approximately 3.14159).
"""

#c
radius=float(input("Enter radius of circle :"))

area= math.pi *(radius**2)
print(round(area,3))

'''List Manipulation
a) Create a list called "fruits" containing the following fruits: "apple", "banana", "cherry", "date", "strawberry", "fig", and "grape". Print the list.
1. Remove the first and last elements from the "fruits" list. Print the updated list.
2. Replace the second to fourth items with ["kiwi", "lemon", "mango"] using list slicing.
3. Use the len() function to find how many fruits are in the list.
'''

#Question 3
 #a)

fruits=["apple", "banana", "cherry", "date", "strawberry", "fig", "grape"]

fruits.pop(0)
fruits.pop()

print(fruits)

#b
fruits[1:4] = ["kiwi", "lemon", "mango"]

print(len(fruits))



"""
a) Create a dictionary named "capitals" with three key-value pairs: "USA" - "Washington D.C.," "France" - "Paris," and "Japan" - "Tokyo." Print the dictionary.
b) Add a new country and its capital to the "capitals" dictionary. The country is "Germany," and the capital is "Berlin." Print the updated dictionary.
c) Check if "France" exists in the "capitals" dictionary. If it does, print "France is in the dictionary," otherwise, print "France is not in the dictionary." 

"""

#Question 4:

capitals={ "USA" :"Washington D.C", "France" : "Paris"  ,"Japan" :"Tokyo"}

capitals["Germany"]="Berlin"

print(capitals)

if "France" in capitals:
    print("France is in the dictionary")
else:
    print("France is not in the dictionary")    


"""a) Create a variable called number that takes user input. 
Write a block of code that checks if the number is positive or negative. 
If the number is positive only then further check if it is even or odd. 
Your output should print “The number is even”, or the “The number is odd”. 
b) Create two variables called age and GPA. Give them values of your choice. 
Next, write a block of code to check if a student with this age and GPA is
 eligible for admission
. The following are the conditions:
   - The student must be at least 18 years old.
   - The student's GPA must be 3.0 or higher on a scale of 4.0.
   Your output should print “Eligible for admission” or “Not eligible for admission”. 
"""

#Question 5:

#a
num=int(input("Enter an integer: "))

if (num>=0):
    if(num%2==0):
        print("the number is even")
    else:
        print("The number is odd")    
else:
    print("Negative Number")        

#b
gpa=float(input("Enter your gpa :"))

age=int(input("Enter your age :"))

if(age>=18 and gpa>=3):
    print("Eligible for admission")
else:
    print("Not eligible for admission ")       


"""Task 6: Strings Manipulation
a) Create a string variable containing the following sentence:
   "Python programming is fun and powerful!"
   Write Python code to do the following and print the results:
   1. Find the length of the string.
   2. Convert the string to uppercase.
   3. Replace "fun" with "exciting."
   4. Check if the string contains the word "Python."
  6. Extract the last word "powerful!"
  5. Remove the word programming from the sentence and print the rest of the sentence.
b) Given the string email = "user@example.com", perform the following:
Extract the username part (everything before the "@" symbol).
Extract the domain part (everything after the "@" symbol).
Check if the email contains the substring "example".
  """    

#a

var= "Python programming is fun and powerful!"

print(len(var))

print(var.upper())

print(var.replace("fun","exciting"))

print(var.__contains__("Python"))

var2=var.split()
var3=var2[-1]
print(var3)

var.replace("programming","")
print(var)


"""Task 7: For Loops and While Loops
a) Given a list of temperatures for a week, write a program that tells you
 how many days were above 25°C.  
temp_list = [26, 28, 32, 36, 30, 25, 24, 22, 20, 18]
for temp > 25, print “Today's temp:  temp, its hot!”
for temp <= 25, print “Today's temp:  temp, it is chilly today!”
"""
#question 7
#a
temp_list = [26, 28, 32, 36, 30, 25, 24, 22, 20, 18]

for x in temp_list:
    if(x>25):
        print("The weather is too hot")
    else:
        print("The weather is chill") 



#b

#1.1. Add to list: [-20, -17, -14, -11, -8, -5, -2, 1, 4, 7, 10, 13, 16, 19, 22, 25, 28] 
num_list=[]
for x in range(-20,29,3):
    num_list.append(x)

print(num_list)

#2.2. Add to list: [110, 112, 114, 116, 118, 120, 122, 124, 126, 128]

num_list2=[]
for x in range(110,129,2):
    num_list2.append(x)

print(num_list2)

#3.3. Print: Multiples of 7 starting from 5 and less than 100.

for x in range(5,100):
    if(x%7==0):
        print(x)


"""

4. Print: The first 20 Fibonacci numbers.
Explanation:
The Fibonacci sequence is a series of numbers where each number is the
 sum of the two preceding ones. It starts with 0 and 1:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34…….
Mathematically, it is defined as:
F(n)= F(n−1) + F(n−2)

"""

#4.
a,b=0,1
for _ in range(20):
    print(a,end=" ")
    temp=a
    a=b
    b=temp+b



"""
c) Use nested loops to display the following pattern.
*
**
***
****
*****
******

 """

num=int(input("enter lines for pattern"))
for x in  range(num):
    for y in range(x):
        print("*",end="")
    print()


"""
d) Write a nested loop through the given list to find pair of numbers that 
sum to a given value.
numbers = [6, 8, 2, 4, 6, 10]
target_sum = 12
Save and print the pairs in tuples.
"""

numbers = [6, 8, 2, 4, 6, 10]
pairs=[]
for x in range(len(numbers)):
    for y in range(x+1,len(numbers)):
        if(numbers[x]+numbers[y]==12):
            pairs.append((numbers[x],numbers[y]))

print(pairs)



"""
e) A student obtains the following grades in his courses.
 Make a list of his scores and write a loop to sum up his total score.
  Also, calculate his percentage.

Courses                 Scores out of 100
Mathematics                    78
Programming                   82
Biology                               65
Physics                               80
Chemistry                          50

Next, use python dictionary to assign grades to the student according to the following
 table:

Percentage   Grade
90-100                 A
80-89                   B+
60-79                   B
40-59                   C
39 and below     F
"""

obtNum=[78,82,65,80,50]
total=0
for x in obtNum:
    total+=x
print(total)

percentage=(total/(100*(len(obtNum))))*100

print(percentage)

gradeDic={(90,100):"A",(80,89):"B+",(60,79):"B",(40,59):"C",(0,39):"F"}

for (low,high),grade in gradeDic.items():
    if(low<=percentage<=high):
        studentGrade=grade
        break

print(total)
print(percentage)
print(grade)    

#  TASK- 8
"""a) Write a function called calculate_area that takes the length and
 width of a rectangle and returns its area.
b) Write a Python function to find the max of three numbers entered by the user.
c) Create a basic calculator program that can perform addition, subtraction, multiplication,
 and division operations. Ask the user to input 2 numbers and the operation they want
  to perform. Print result accordingly.
"""

#a
def calculateArea(width,height):
    return width*height

ans=calculateArea(12,24)
print(ans)

#b
def maxNum(a,b,c):
    max=0
    if (a>b and a>c):
        max=a
    elif (b>a and b>c):
        max=b
    else:
        max=c
    print(max)
    return max

maxNum(4,8,6)    


#c

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation \n(\n+, \n-,\n *, \n/): ")

if operation == "+":
    result = num1 + num2
    print(f"The result of {num1} + {num2} is {result}")
elif operation == "-":
    result = num1 - num2
    print(f"The result of {num1} - {num2} is {result}")
elif operation == "*":
    result = num1 * num2
    print(f"The result of {num1} * {num2} is {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation! Please enter one of +, -, *, or /.")
