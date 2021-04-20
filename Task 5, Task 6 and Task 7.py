#Task 5
#File Handling and Exception Handling

'''1. Write a program in Python to allow the error of syntax to be handled using exception handling
HINT: Use Syntax Error'''

def program():
    try:
        eval('a=====b')
    except SyntaxError:
        print("Syntax error")

program()

'''2. Write a program in Python to allow the user to open a file by using the argv module. If the
entered name is incorrect throw an exception and ask them to enter the name again. Make sure
to use read only mode.'''
#default is reading
import sys
for arg in sys.argv[1 :] :
    try :
        f = open ('files.txt', 'r' )
    except FileNotFoundError:
        print ( 'cannot open', arg )
    else :
        print ( arg, 'has', len ( f.readlines () ), 'lines' )
        f.close ()

#3. Write a program to handle an error if user entered a number more thanfour digits it should return
#rethrn "The length is too short/long !!!! Please provide only four digits
try:
    input1 = int(input("Please enter a number greater than 4 or less than 4: "))
    assert len(input1) == 4
except TypeError:
    print('"The length is too short/long !!!! Please provide only four digits')

'''4. Create a login page backend to ask users to enter the username and password. Make sure to
ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
should not be more than 3 times.'''

user_profile_name = input("please type your username: ")
user_profile_password = input("please type your password: ")
k = 1
while k <= 4:
    try:
        if k == 4:
            raise Exception
        k = k + 1
        type_again = input("Please type the password again: ")
        if user_profile_password == type_again:
            break
    except Exception:
        print("you have tried more than 3 times")
    break
#Task 6
#GENERATORS, LIST COMPREHENSION AND DECORATORS'''

'''1.1. Write a program in Python to find out the character in a string which is uppercase using list
comprehension.'''
input = input("please type a word: ")
list1 = [i for i in input if i.isupper()]
print(list1)

'''2. Write a program to construct a dictionary from the two lists containing the names of students and
their corresponding subjects. The dictionary should map the students with their respective subjects.
Let’s see how to do this using for loops and dictionary comprehension.
HINT - Use Zip function also'''
#using zip
students = ['Smit','Jaya','Rayyan']
subjects = ['CSE','Networking','Operating System']
print(dict(zip(students,subjects)))

#using for loop
empty_dict = {}
for key in students:
    for value in subjects:
        empty_dict[key] = value
        subjects.remove(value)
        break
print("dictionary is: ",str(empty_dict))

#using list_comprehension
new_dict = {x: y for (x,y) in zip(students, subjects)}
print("new dictionary is: " + str(new_dict))

'''3. Learn more About yield, next and Generators'''
'''def simpleGeneratorFun():
    yield 1            
    yield 2            
    yield 3            
   
# Driver code to check above generator function
for value in simpleGeneratorFun(): 
    print(value)'''

'''yield = yield is a keyword in Python that is used to return from a function without destroying the states of its local variable
 and when the function is called, the execution starts from the last yield statement.'''
'''next = The next() function returns the next item in an iterator.
generator = Python generators are a simple way of creating iterators. All the work we mentioned above are automatically handled by generators in Python.
'''

'''4.  Write a program in Python using generators to reverse the string.
Input String = “Consultadd Training”'''

input_string ="Consultadd Training"
def new_Function(input_string):
    for i in range(len(input_string)-1, -1, -1):
        yield input_string[i]

new_input= new_Function(input_string)
print(new_input.__next__())
print(new_input.__next__())
print(new_input.__next__())

for i in new_input:
    print(i)

'''6. Given an example of decorator'''


def attach_data(func) :
    func.data = 3
    return func


@attach_data
def add(x, y) :
    return x + y


print ( add ( 2, 3 ) )
# 5
print ( add.data )

#Task 7
'''1.1. Write a program that calculates and prints the value according to the given formula:
Q= Square root of [(2*C*D)/H]
Following are the fixed values of C and H:
C is 50.
H is 30.
D is a variable whose values should be input to your program in a comma-separated sequence.
'''
import math

asking_user = input("Choose a value")
asking_user = asking_user.split(',')

result_list = []
for D in asking_user:
    Q = round(math.sqrt(2 * 50 * int(D) / 30))
    result_list.append(Q)

print(result_list)
'''2. 2. Define a class named Shape and its subclass Square. The Square class has an init function which
takes length as argument. Both classes have an area function which can print the area of the shape
where Shape’s area is 0 by default.'''
class Circle():
    def __init__(self,r):
        self.radius = r

    def area(self):
        return 3.1416*(self.radius**2)


circle = Circle(5)
print(circle.area())


'''3.  Create a class to find three elements that sum to zero from a set of n real numbers
Input array: [-25,-10,-7,-3,2,4,8,10]
Expected output: [[-10,2,8],[-7,-3,10]]'''

class py_solution:
 def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))

'''5.. Write a Person class with an instance variable “age” and a constructor that takes an integer as a
parameter. The constructor must assign the integer value to the age variable after confirming the
argument passed is not negative; if a negative argument is passed then the constructor should set
age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance
methods:
yearPasses() should increase age by the integer value that you are passing inside the function.
amIOld() should perform the following conditional actions:I
f age is between 0 and <13, print “You are young”.
If age is >=13 and <=19 , print “You are a teenager”.
Otherwise, print “You are old”.
'''
class Person:
    age = 0
    def __init__(self,initialAge):
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
        else:
            self.age = initialAge
    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1


'''4.'''
class Time():

  def __init__(self, hours, mins):
    self.hours = hours
    self.mins = mins

  def addTime(t1, t2):
    t3 = Time(0,0)
    if t1.mins+t2.mins > 60:
      t3.hours = (t1.mins+t2.mins)//60
    t3.hours = t3.hours+t1.hours+t2.hours
    t3.mins = (t1.mins + t2.mins) % 60
    return t3

  def displayTime(self):
    print ("Time is",self.hours,"hours and",self.mins,"minutes.")

  def displayMinute(self):
    print ((self.hours*60)+self.mins)

a = Time(2,40)
b = Time(1,30)
c = Time.addTime(a,b)
c.displayTime()
c.displayMinute()