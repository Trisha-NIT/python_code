# 1. Given a list, iterate it, and display numbers divisible by five, and if you find a number greater than 150, stop the loop iteration.

from typing import List


numbers = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

i = 0

for number in numbers:
    if (numbers[i]) % 5 == 0:
       print(numbers[i])
       if numbers[i]>150:
        break
    i=i+1

# 2. Reverse the List 

list1 = [10, 20, 30, 40, 50]

i = 4

for number in list1:
    print(list1[i])
    i = i-1  

# 3.Display numbers from -10 to -1 using for loop  

for numbers in range (-10,0):
    print(numbers)


# 4.Display a message “Done” after successful execution of for loop

for i in range(5):
    print (i, end=",")
print("Done!")


# 5.Create a function that can accept two arguments name and age and print its value

def person(name,age):
      print(name,age)

person("Rishi",30)

# 6. Create a function showEmployee() in such a way that it should accept employee name, and its salary 

def showEmployee(name,salary=9000):
    print(name,salary)

showEmployee("Ben",9000)
showEmployee("Ben")

# 7. Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of them

def calculation(a,b):
    subtraction = a-b
    addition = a+b
    return subtraction,addition

c = calculation(50,40) 
print(c)

#8. Generate a Python list of all the even numbers between 4 to 30

list = []
for i in range(6,30,2):
    list.append(i)

print(list)    


#9. Return the largest item from the given list  

List = [4, 6, 8, 24, 12, 2]

x = 0

a = List[0]
c = a
while x<5:
    b = List[x+1]
    if c>b:
        c = c
    else:  
        c = List[x+1]
    x=x+1   
print(c)    


List = [4, 6, 8, 24, 12, 2]
   
print(max(List))


# 10.Below are the two lists convert it into the dictionary

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]

dictionary = dict(zip(test_keys, test_values))
  
print (dictionary)

# def list_to_dict(test_keys,test_values)
new_dict = {test_keys[i]:test_values[i]  for i in range(len(test_keys)) }
#     return new_dict

# result = list_to_dict(test_keys,test_values)
print(new_dict)      
 
 


