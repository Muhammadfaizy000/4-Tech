# questions= [
#     {
#         "s.no": "1",
#         "question": "what is your name",
#         "option": ["ali","ahemed","zain"],
#         "answer": "ali"
#     },
#     {
#         "s.no": "2",
#         "question": "what is your age",
#         "option": ["18","23","24"],
#         "answer": "23"
#     },{
#         "s.no": "3",
#         "question": "what is your city name",
#         "option": ["karachi","ahemed","zain"],
#         "answer": "karachi"
#     }

# ]

# score=0
# for quiz in questions:
#     data= quiz["s.no"] +"," + " "+ quiz["question"] + "\n" + quiz["option"][0]+ "\n" + quiz["option"][1]+ "\n" + quiz["option"][2]+ "\n"
#     answer=input(data)
#     if answer==quiz["answer"]:
#         score+=1
# print (score)



# def add(a=4, b=6):
#     print (a+b)
# def add(a , b):
#     print (a+b)
# add(2,9)


#question 9

lst=[1,3,4,6,3]
a=len(lst)
print(a)

#question 10
#.Write a Python program to sum all the numeric items in a list?

list1=[1, 5 , 4]
sum=0
for i in list1:
    sum+=i

print(sum)


#question 11
list2=[ 1,5,6,3,8]
data=0
for i in list2:
    if data<=i:
        data=i
print(data)

#question 12
a=  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
   if i < 5:
       print(i)


# question 13
 

# Define a list of mixed values
my_list = ["apple", 3, "banana", 5.6, "orange"]

# Initialize a flag variable to False
has_numeric = False

# Loop through the list
for item in my_list:
  # Check if the item is a numeric value (int or float)
  if isinstance(item, (int, float)):
    # Set the flag to True and break the loop
    has_numeric = True
    break

# Print the result
if has_numeric:
  print("The list has a numeric value.")
else:
  print("The list has no numeric value.")


#question 10
  # Define a list of mixed values
my_list = ["apple", 3, "banana", 5.6, "orange"]

# Initialize a sum variable to zero
total = 0

# Loop through the list
for item in my_list:
  # Check if the item is a numeric value (int or float)
  if isinstance(item, int):
    # Add the item to the sum
    total += item

# Print the result
print("The sum of all the numeric items in the list is", total)


#question 2 ass 4
# Define a dictionary
my_dict = {"name": "Ali", "age": 25, "city": "Karachi"}

# Print the original dictionary
print("The original dictionary is", my_dict)

# Define a new key and value to add
new_key = "country"
new_value = "Pakistan"

# Add the new key and value to the dictionary
my_dict[new_key] = new_value

# Print the updated dictionary
print("The updated dictionary is", my_dict)



#question 3 ass 4
# Define a dictionary of mixed values
my_dict = {"name": "Ali", "age": 25, "city": "Karachi", "salary": 50000, "country": "Pakistan"}

# Initialize a sum variable to zero
total = 0

# Loop through the dictionary values
for value in my_dict.values():
  # Check if the value is a numeric value (int or float)
  if isinstance(value, (int, float)):
    # Add the value to the sum
    total += value

# Print the result
print("The sum of all the numeric items in the dictionary is", total)


#question 5
List=[1,3,4,56,3,8,9,2]
List1=[]
for i in List:
   if i not in List1:
        List1.append(i)
print(List1)

#question 6 ass 4
# Define a dictionary
my_dict = {"name": "Ali", "age": 25, "city": "Karachi"}

# Define a key to check
key = "age"

# Check if the key is in the dictionary using the in operator
if key in my_dict:
  print("The key", key, "already exists in the dictionary.")
else:
  print("The key", key, "does not exist in the dictionary.")
