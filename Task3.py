#Task Three
#Data Structures

''' 1. Create a list of 10 elements of four different data types like int, string, complex and float'''

new_list = ['s',1,complex(1,3),True,1.0,2.0,'Shekhar',3,False,'abc']
print(new_list)

'''2. Create a list of size 5 and execute the slicing structure'''
a = [1,2,3,4,5]
new_var = a[0:4] #start:stop:step
print(new_var)

'''3. Wrtie a program to ge the sum and multiply all the items in a given list'''

list1 = [2,2,2,2]
total = 0
multiply = 1
for i in range(len(list1)):
    total=total+list1[i]
print("Sum of element in given list is: ", total)
for j in range(len(list1)):
    multiply = multiply*list1[i]
print("Multiplication of element in given list is: ",multiply)


'''4. Find the largest and smallest number from a given list'''

data2 = [0,1,2,3,4,5]
min = data2[0]
max = data2[0]
for i in data2:
    if min > i:
        min = i
    if max < i:
        max = i

print("min is = ", min)
print("max is = ", max)


'''5. Create a new list which contains the specified numbers after removing the even numbers from a
predefined list.'''

odd_and_even_list = [2,4,1,3,5]
odd_list = []
for i in range(len(odd_and_even_list)):
    if i %2 != 0:
        odd_list.append(i)
print("The new list with odd number is ", odd_list)



'''6. Create a list of elements such that it contains the square of first and last 5 elements between 1 and 30 both included'''

squared_list = []
for i in range(1,31):
    if i <= 5:
        squared_list.append(i * i)
    if i > 25:
        squared_list.append((i * i))
print(squared_list)



'''7. Write a program to replace the last element in a list with another list. Sample input: [1,3,5,7,9,10], [2,4,6,8]
Expected output: [1,3,5,7,9,2,4,6,8]'''

sample_input = [1,3,5,7,9,10]
list2 = [2,4,6,8]
sample_input.remove(sample_input[-1])
result = sample_input + list2
print(result)

'''8. Create a new dictionary by concatenating the following two dictionaries: Sample input: a={1:10,2:20} b={3:30,4:40)
Expected output: {1:10,2:20,3:30,4:40}'''
a={1:10,2:20}
b={3:30,4:40}
new_dict = {}
for i in [a,b]:
    new_dict.update(i)
print(new_dict)

'''9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
and n(both 1 and n included).'''
n = 3
a = {}

for i in range(1, 4):
    a[i] = i * i
print(a)



