'''1. Create a list of given structure and get the Access list as provided below'''
'''x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
Access list: [1, 2, 3, 4]Access list: [600, 700]
Access list: [100, 300, 500, 600, 800]
Access list: [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
Access list: [10]
Access list: [ ]'''

x = [100, 200, 300, 400, 500, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 600, 700, 800]
x = [100, 200, 300, 400, 500, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 600, 700, 800]
variable = [x[index] for index in [0, 2, 4, 6, 8]]

print("Access List:", x[5][0:4])
print("Access List:", x[-3:-1])
print("Access List:", variable)
print("Access List:", x[::-1])
print("Access List:", x[5][5][0])

'''2. Create a list of thousand numbers using range and xrange and see the difference between each
other.'''
list = []
for i in range(0, 1000):
    list.append(i)
print(list)

# list2 = []
# for z in xrange(0,1000):
# list2.append(z)
# print(list2)
# I read on the website and it said xrange named got change to range in Python 3. therefore, I got an error saying
# xrange is not defined. Xrange has better speed and require less memory. When you have to traverse the list frequently, then
# its better to use range().

'''3. How is tuple benefitial compared to list?'''
'''Ans = Tuples are fined size in nature i.e. we can't add/delete elements to/from a tuple. We can search any element in a tuple. Tuples are faster than lists, because they have 
a constant set of values. Tuples can be used as dictionary keys, because they contain immutable values like strings, numbers, etc.'''

'''4. Write a program in Python to iterate through the list of numbers in the range of 1,100 and print
the number which is divisible by 3 and is a multiple of 2.'''
for i in range(1, 1000):
    if i % 5 == 0 and i %2 == 0:
        print(i)

'''5. Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the
string with their index.'''
new_var = str(input("Enter a word to reverse it: "))
reversed_string = new_var[::-1]
print("The reversed of the input of: ", new_var, "is", reversed_string)
vowels = 'a', 'i', 'e', 'o', 'u', 'A', 'I', 'E', 'O', 'U'
new_word = []
for i in reversed_string:
    if i in vowels:
        new_word = reversed_string.replace(reversed_string,i)
        print("The index of the vowel",new_word, "in reversed string is: ",reversed_string.index(new_word))
else:
    pass

'''6. Write a program in Python to iterate through the string “hello my name is abcde” and print the
string which is having an even length.'''

string = "hello my name is abcde"
new_string = string.split()
new_list = []
for i in new_string:
    if len(i) %2 == 0:
        new_list.append(i)
print(new_list)

'''7.Write a program in python to print the pair of numbers whose sum is equal to the result
number that is let's say 8. '''
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1]
n = len(a)


def sum_pair(arr, n, s):
    result = []
    for i in range(0, n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j]  ==  s):
                result.append([arr[i], arr[j]])
    return result


print(sum_pair(a, n, 8))

'''8. Write a program in Python to complete the following task:
Create two lists such as even_list and odd_list
Ask user to enter a number in the range of 1,50 and make sure if the entered number is
even, append it to the even_list and if the entered number is odd append it to the odd_list.
Keep that in mind you can only add 5 items in each list
Make sure once you enter all the 5 elements, calculate the sum of the list and return the
maximum of the list.
'''
even_list = []
odd_list = []
while True :
    asking_user2 = int ( input ( "please enter a number between 1 and 150: " ) )
    if asking_user2 in range ( 1, 150 ) :
        if asking_user2 % 2 == 0 :
            even_list.append ( asking_user2 )
            print ( "This went to the even list because", asking_user2, "is even", even_list )
        elif asking_user2 % 2 != 0 :
            odd_list.append ( asking_user2 )
            print ( "This went to the odd list because", asking_user2, "is odd", odd_list )
    if len ( even_list ) >= 5:
        print ( "the sum of even list is", sum ( even_list ) )
        print("the max of even list is", max(even_list))
        break
    elif len(odd_list) >= 5:
        print("the sumof odd list is",sum(odd_list))
        print("the max of odd list is",max(odd_list))
        break



'''9. Write a program to find out the occurrence of a specific character from an alphanumeric string. Sample input: 12abcbacbaba344ab Expected output: a=5 b=5 c=2'''

string = "12abcbacbaba344ab"
print("same letter in word", string)

output = {y: string.count(y) for y in set(string) if y.isalpha()}

print("Expected Output: \n" + str(output))

''' 10 Generate and print another tuple whose values are even numbers in the given tuple
(1,2,3,4,5,6,7,8,9,10).'''

tuple_here =(1,2,3,4,5,6,7,8,9,10)
new_tuple = []
for i in tuple_here:
    if i % 2==0:
        new_tuple.append(i)
tuple = tuple(new_tuple)
print("The new tuple is",tuple)
