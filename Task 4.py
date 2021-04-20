# Task 4
'''1. Write a program to reverse a string'''

sample_input = "1234abcd"
sample_input = sample_input[: :-1]
print ( sample_input )

'''2. Write a function that accepts a string and prints the number of uppercase letters and lowercase
letters.'''
lower_count = 0
upper_count = 0
asking_user = str ( input ( "Enter a word to count the lower case and uppercase charcaters: " ) )
for i in asking_user :
    if i.islower () :
        lower_count += 1
        i.count ( i )
    else :
        upper_count += 1
        i.count ( i )
print ( "The total length of lower case letter is: ", lower_count )
print ( "The total of upper case letter is: ", upper_count )

'''3. Create a function that takes a list and returns a new list with unique elements of the first list.'''
list_1 = [2, 3, 2, 4, 5, 4, 5]


def unique_list(list_1) :
    u_list = set ( list_1 )
    return list ( u_list )


print ( unique_list ( list_1 ) )

'''4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
in a hyphen-separated sequence after sorting'''

hyphen = input ( "Enter hyphen-seperated sequence of words: " )
splitting = hyphen.split ( '-' )
splitting.sort ()
new_word = ('-'.join ( splitting ))
print ( new_word )

'''5. Write a program that accepts a sequence of lines as input and prints the lines after making all
characters in the sentence capitalized.'''

asking_user1 = str ( input ( "Enter a sentence to turn it into all caps: " ) )
upper = asking_user1.upper ()
print ( upper )

'''6. Define a function that can receive two integral numbers in string form and compute their sum and
print it in the console.'''

def add(x,y):
    c = int(x) + int(y)
    return c

x = input("Etner a number")
y = input("Enter a number")
print(add(x,y))

''' 7. Define a function that can accept two strings as input and print the string with the maximum length
in the console. If two strings have the same length, then the function should print both the strings line
by line.'''

def max_length(first,second):
    count_for_first_word = 0
    count_for_second_word = 0
    for j in first:
        if j.isalpha():
            count_for_first_word += 1
            j.count(j)
    for k in second:
        if k.isalpha():
            count_for_second_word += 1
            k.count(k)

    if count_for_first_word > count_for_second_word:
        print("printing first word because the character of first word is",first, "is", count_for_first_word)
    elif count_for_first_word < count_for_second_word:
        print ( "printing second word because the character of first word is", second, "is", count_for_second_word )
    elif count_for_first_word == count_for_second_word:
        print(first,second)

first = input("Enter a word: ")
second = input("Enter another word: ")
max_length(first,second)

'''8. Define a function which can generate and print a tuple where the values are square of numbers
between 1 and 20 (both 1 and 20 included).'''
list_first_tuple_second = []


def square() :
    for i in range ( 0, 21 ) :
        i *= i
        list_first_tuple_second.append ( i )
    print(list_first_tuple_second)
    new_list = tuple(list_first_tuple_second)
    print(new_list)


square ()

'''9. Write a function called showNumbers that takes a parameter called limit. It should print all the
numbers between 0 and limit with a label to identify the even and odd numbers. Sample input: show Numbers(3) (where limit=3)
Expected output:
0 EVEN
1 ODD
2 EVEN
3 ODD'''

def checking(limit): #parameter called limit
    for i in limit:
        if i %2 == 0:
            print(i, "EVEN")
        if i%2 != 0:
            print(i, 'ODD')
limit = range(0,100)
checking(limit)


def checking(limit): #parameter called limit
    for i in range(limit):
        if i %2 == 0:
            print(i, "EVEN")
        if i%2 != 0:
            print(i, 'ODD')


checking(4)

'''10. Write a program which uses filter() to make a list whose elements are even numbers between 1
and 20 (both included) '''

l1 = range(1,21)
print(list(filter(lambda x: x % 2 ==0, l1)))

'''
11. Write a program which uses map() and filter() to make a list whose elements are squares of even
numbers in [1,2,3,4,5,6,7,8,9,10].
Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the
numbers in the filtered list. Use lambda() to define anonymous functions.'''
list_1 = [1,2,4,5,6,7,8]
print(list(map(lambda x: x * x,(filter(lambda x: x % 2 == 0, list_1) ))))

'''12.Write a function to compute 5/0 and use try/except to catch the exceptions'''
number = 5
try:
    divisible = number/0
except ZeroDivisionError:
    print("cant divide by zero")
finally:
    print("Execution")
'''13.Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().'''

from functools import reduce
flatten_list = [1,2,3,4,5,6,7]
d=reduce(lambda new, d: 10 * new + d, flatten_list)
print(d)

'''14.Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
Make sure to use only higher order functions.'''


list1 = range(1,51)
print(list(filter(lambda x: x %3 !=0 and x%7 == 0, list1)))

'''15.Write a program in Python to multiply the elements of a list by itself using a traditional function
and pass the function to map() to complete the operation.'''

def multiplying(i):
    return i * i



list1= range(1,5)
print(list(map(multiplying,list1)))

'''16. What is the output of the following program.'''

def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)
#output = 2
'''

def a():
    try:
        f(x, 4)
    finally:
        print('after f')
        print('after f?')
a()
'''
#output after f? after f? f is not defined

