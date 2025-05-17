# Data Structures of list.
# List: A list is a list but changeable after creation
fruits = ["apple", "banana", "mango"]
print (fruits[0])
fruits.append("grapes")
fruits[1]="kiwi"
print(fruits)

# Data Structures of Tuple 
# Tuple : A tuple is like a list but unchangeable after creation
colors =("red", "green","blue")
print(colors[1])
# You can't do like this : 
# colors [1] = "yellow"

# Data Structures of Set 
# Set : A set is like a bag it doesn't care about order and automatically removes duplicates 
nums = {1,2,3,3,4}
print(nums)
nums.remove(2)

# Data Structures of Dictionary 
# Dictionary : Dictionary is a like a real dictionary which Keys must be unique and immutable (strings, numbers, tuples)

student = {"name": "shyam", "age": 20, "grade": "A"}
print(student["name"])      # shyam
student["age"] = 21         # modify
student["city"] = "Dolakha"  # add new key
print (student ["age"])

