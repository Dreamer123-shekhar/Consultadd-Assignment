#Task 2
#Operators and Decision making statement

'''1. Write a program in Python to perform the following operation:
If a number is divisible by 3 it should print “Consultadd” as a string
If a number is divisible by 5 it should print “Python Training” as a string
If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a
string.'''

newUser = int(input("Enter a number: "))
if newUser %3 == 0 and newUser %5 != 0:
    print("Consultadd")
elif newUser %5 == 0 and newUser %3 != 0:
    print("Python Training")
elif newUser %5 == 0 and newUser %3 == 0:
    print('Consultadd - Python Training')


'''2. Write a program in Python to perform the following operator based task
Ask user to choose the following option first:
If User Enter 1 - Addition
If User Enter 2 - Subtraction
If User Enter 3 - Division
If User Enter 4 - Multiplication
If User Enter 5 - Average
Ask user to enter two numbers and keep those numbers in variables num1 and num2
respectively for the first 4 options mentioned above.
Ask the user to enter two more numbers as first and second for calculating the average as
soon as the user chooses an option 5.
At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
NOTE: At a time a user can only perform one action.
'''
average = 0
asking_user = int(input('Please Enter a number between 1 to 5: '))
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if asking_user == 1 and num1 + num2 > 0:
    print(num1 + num2)
    print("you selected addition option")
elif asking_user == 2 and num1 - num2 > 0:
    print(num1 - num2)
    print("you selected Subtraction option")
elif asking_user == 3 and num1 // num2 > 0:
    print(num1/num2)
    print("you selected Division")
elif asking_user == 4 and num1 * num2 > 0:
    print(num1 * num2)
    print("you selected Multiplcation")
elif asking_user == 5:
    third = int(input("Enter the first number: "))
    fourth = int(input("Enter the fourth number: "))
    average = (num1 + num2 + third + fourth)//4
    if average < 0:
        print('Negative average')
else:
    print("Negative")


''''4 
Write a program in python to break and continue if the following cases occur

If user enters a negative number just break the loop and print “It’s Over”
If user enters a positive number just continue in the loop and print “Good Going”
'''

while True:
    answer1 = int(input("Enter a positive number to continue this loop or negative number to break it: "))
    if answer1 > 0:
        print("Good Going")
        continue
    elif answer1 < 0:
        print("It's over")
        break

print("Have a nice day")

''' 6 what is the output of the following code examples'''

'''x = 123
for i in x:
    print(i)
#int object is not iterable'''


'''i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
    else:
        print("error")
output = 0 error 1 error 2'''

''''count = 0
while True:
    print(count)
    count += 1
    if count >=5:
        break
output = 0, 1,2,3 4'''



'''7 Write a program that prints all the numbers from 0 to 6 except 3 and 6'''
'''Expected outcome 0,1,2,3,4,5'''
'''Note use continue statement'''

for x in range(6):
    if x == 3 or x ==6:
        continue
    print(x, end= ' ')

#or solution 2 for same question
i = - 1
while i < 6:
    i = i + 1
    if i == 3 or i==6:
        continue
    print(i)


'''5 Write a program in which it will find all such numbers which are divisble by 7 but are not a multiple of 5, between 2000 and 3200  '''
for i in range(2000,3200):
    if i %7 == 0 and i% 5!=0:
        print(i)

'''8 Write a program that accepts a string as an input from the user and calculate the number of digits and letters.
Sample input: consul72 Expected output: Letters 6 Digits 2'''

numeric_count = 0
alpha_count = 0
user_question = input("Please type something with both numeric and alphabetic characters: ")
for s in user_question:
    if s.isnumeric() == True: #you can do == True or just leave s.isnumeric()both is correct
        numeric_count = numeric_count + 1
    elif s.isalpha():
        alpha_count = alpha_count + 1
print("The total number of string is", alpha_count)
print("The total number of digit is", numeric_count)


'''9.. Read the two parts of the question below:
a) Write a program such that it asks users to “guess the lucky number”. If the correct number is
guessed the program stops, otherwise it continues forever.
b) Modify the program so that it asks users whether they want to guess again each time. Use two
variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
The program continues as long as a user has not answered “no” and has not guessed the correct
number)'''
while True:
    guess_number = 5
    asking_user = int(input("Guess a number between 1 to 5: "))
    if asking_user != guess_number:
        print("Keep trying")
        continue
    elif asking_user == guess_number:
        print("breaking the loop")
        break

'''10 Write a program that asks five times to guess the lucky number. Use a while loop and a counter, such as
counter=1 While counter <= 5:
print(“Type in the”, counter, “number”
counter=counter+1
The program asks for five guesses (no matter whether the correct number was guessed or not). If the
correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
After the fifth guess it stops and prints “Game over!”.'''

counter = 1
lucky_number = 7
while counter <= 5:
    user_input = int(input("Choose a number between 3 and 7: "))
    counter += 1
    if (user_input == lucky_number):
        print("good guess")
    elif counter <= 5:
        print("Try again")
print("game over")

'''11. In the previous question, insert break after the “Good guess!” print statement. break will terminate
the while loop so that users do not have to continue guessing after they found the number. If the user
does not guess the number at all, print “Sorry but that was not very successful”.'''

counter = 1
lucky_number = 7
while counter <= 5:
    user_input = int(input("Choose a number between 3 and 7: "))
    counter += 1
    if (user_input == lucky_number):
        print("Good guess")
        break
    elif counter <= 5:
        print("Try again")
print("game over")