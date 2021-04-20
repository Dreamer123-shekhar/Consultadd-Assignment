#T1
#Number and variables
#1
'''Create three variables in a single line and assign values to them in such a manner that each one of
them belongs to a different data'''

e, b, c = 100, 'string', True
print(e,b,c)

#2
#Create a variable of type complex and swap it with another variable of type integer.


#creating a comple variable
complex_variable = 5 + 2j
integer_variable = 2
#swapping values
complex_variable, integer_variable = integer_variable,complex_variable
print(complex_variable,integer_variable)

#Swap two number using a third variable and do the same task without using third variable

#swapping to number using third variable
n = 5
n1 = 6
n3 = n
n = n1
n1 = n3
print(n, n1)

#two number without using third variable
abc = 4
abc1 = 6
abc, abc1 = abc1, abc
print(abc, abc1)

#7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
#UPPERCASE.
#(Refer: https://capitalizemytitle.com/camel-case/)


UpperCamelCase = 'ShekharCamel'
lowerCamelCase = 'lowerCamelCase'
this_is_how_you_write_snakecase = 'hello'
UPPERCASE = 'UPPERCASE'

#4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x version

name = input("Enter your name :")
print("Hello {} !".format(name))


# 6. Write a program to check the data type of the entered values.
#HINT: Printed output should say - The data type of the input value is : int/float/string/etc
checking_data_type = 'here'
print(checking_data_type, "The data type of the input value is", type(checking_data_type))



#8If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
#again. Will it change the value? If Yes then Why?

a = 100
print(hex(id(a)))
a = 200
print(hex(id(a)))

#Here we can see everytime we create a new variable it is stored in a different memory id
#Yes, it will change because python recognizes thew new value assigned to a and it does not recognize the old value.

'''5 Write a program to complete the task given below:
Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
another variable called z. Add 30 to z and store the output in variable result and print result as the
final output'''

first_value = int(input("Enter the first number between 1 and 10: "))
second_value = int(input("Enter the second number between 1 and 10: "))
z = first_value + second_value
final_output = 30 + z
print(f'The final output is  {final_output}')



