# Control Flow : Control flow determines which lines of codes get executed and order and under what conditions 
# The three main types : 
# 1) Conditional Statements : if, elif, else
# 2) Loops : for and while 
# 3) Loop Control Statements: break, continue, pass 

#Conditional Statements 
age = int (input("Enter Your age: "))
if age > 18 : 
    print("You can vote")
elif age >= 13: 
    print("You are a teenager")
else : 
    print("You are a child")

# For Loop 
shopping_list = ["milk", "bread", "eggs", "rice"]
for item in shopping_list:
    print("Buy: ", item)

# while loop 
correct_password = "1234"
user_input = ""

while user_input != correct_password:
    user_input = input("Enter password: ")

print("Access granted!")

# Break and Continue 
numbers = [1,3,7,8,11,14]
for num in numbers : 
    if num %2 == 0 :
        print("First even number is : ", num)
        break 
#pass 
for i in range(5):
    if i == 5:
        pass  
    print("Number:", i)

#else with loops 
names = ["Ramu", "Harry", "Shyam"]

for name in names:
    if name == "Gita":
        print("Gita found!")
        break
else:
    print("Gita not in the list.")
