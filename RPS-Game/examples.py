import random

#Example Calling functions
def greeting():
    return 'Hi'
response = greeting()
print(response)

#Exmaple if, else, elif
age = 20
if age >= 18:
    print('You are an adult.')
elif age > 12:
    print('You are a teenager.')
elif age > 1:
    print('You are a child.')
else:
    print('You are a baby.')


#Example f string
age = 25
print(f'Jim is {age} year old.')


#Example Data Type and Casting
name = 'something'
print(type(name))
print(isinstance(name, str))
age = 2 #can make it float by float(2)
print(isinstance(age, float)) #false since it's not a decimal number

#complex for complex numbers
#bool for booleans - String, list, tuple, dict, and set is false only when empty. All numbers is True except for 0 which is False
#list for lists - A collection which is ordered and changeable. Allows duplicate members.
#tuple for tuples - A collection which is ordered and unchangeable. Allows duplicate members.
#range for ranges
#dict for dictionaries - A collection which is ordered and changeable. No duplicate members.
#set for sets - A collection which is unordered, unchangeable, and unindexed. No duplicate members. Can remove and/or add items whenever you like.

#Example Tuples
#Uses ( )
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")

#Exmaple List
#Uses [ ]
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
food = ['pizza', 'carrots', 'eggs']
dinner = random.choice(food)
print('pizza' in food) #True
print(food[0]) #pizza
print(food[-1]) #eggs
print(food[0:2]) #splicing; going from index 0 to 1 and stop at 2(does not include 2); pizza, carrots
print(food[1:]) #carrots, eggs
print(food[:1]) #pizza
print(len(food)) #3
food.append('pie') #adding an object to the list; add pie to the list 
food.extend(['apple', 'cake']) #can add another list by using extend
#food += ['apple, cake'] same as above; same as extend
food.remove('apple') #removing from list; remove apple from list
print(food.pop()) #remove and return the object at the end of the list (last item of the list)
food.insert(2, 'salt') #insert an item at a certain index of a list; insert salt at index 2
food[1:1] = ['banana', 'cherry'] #adding multiple items to list; add banana and cherry at index 1 [pizza, banana, cherry...]
#sorting modify the original list content, so save it in another variable
foodCopy = food[:]
food.sort() #sort the list by alphabetical order; Uppercase letter first then lower case
food.sort(key=str.lower) #ignoring the cases and sort in alphabetical order
print(sorted(food, key=str.lower)) #can use the sorted global function to not modify original list
food[2] = 'milk' #updating list; changing eggs to milk


#Example Dictionaries
#Uses { }
dict = {'name': 'beau', 
        'color': 'blue'}
thisdict = {
    "brand": "Ford", #string
    "electric": False, #boolean
    "year": 1964, #int
    "colors": ["red", "white", "blue"] #list
    } 

#Example Sets
#Uses { }
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False} 


#Example Arthimetic Operators
1 + 1 #2 - addition
2 - 1 #1 - subtraction
2 * 2 #4 - multiplication
4 / 2 #2 - division
5 % 3 #2 - remainer
4 ** 2 #16 - exponoent
5 // 2 #2 - floor division

print('Scamp' + ' is a good dog')

age = 8
age += 8 #age = age + 8


#Example Comparison Operators
a = 1
b = 2

a == b #False - a is equal to b
a != b #True - a is not equal to b
a > b #False - a is greater than b
a <= b #True - a is less than or equal to b


#Example Boolean Operators
condition1 = True
condition2 = False

not condition1 #False
condition1 and condition2 #False
condition1 or condition2 #True


#Example is and in Operators
#is - an identity operator; use to compare two objects and return true if both are the same object
#in - a membership operator; use to tell if a value is contain in a list or another sequence
name = 'Beau'
print('au' in name) #True


#Example Ternary Operator
#Slow way
def is_adult1(age):
    if age > 18:
        return True
    else:
        return False
#Ternary
def is_adult2(age):
    return True if age > 18 else False


#Example any and all
#any return True if any is true
#all return True if all is true
ingrediants_purchased = True
meal_cooked = False
ready_to_serve = any([ingrediants_purchased, meal_cooked]) #True
ready_to_serve = all([ingrediants_purchased, meal_cooked]) #False


#Example complex number
num1 = 2+3j
num2 = complex(2,3) #2 is the real number, 3 is the imaginary
print(num1.real, num2.imag)


#Example Built-in Functions
print(abs(-5.5)) #absolute - 5.5
print(round(5.49)) #round - 5
print(round(5.49, 1)) #round to the nearest decimal point 5.5

#Example Enum
from enum import Emum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State.ACTIVE) #State.ACTIVE
print(State.ACTIVE.value) #1
print(State(1)) #State.ACTIVE
print(State['ACTIVE']) #State.ACTIVE
print(State['ACTIVE'].value) #1
print(list(State)) #[<State.INACTIVE: 0>, <State.ACTIVE: 1>]
print(len(State)) #2


