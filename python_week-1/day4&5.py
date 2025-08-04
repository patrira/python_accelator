my_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
tropical = ["mango", "pineapple", "papaya"]
this_list = ["apple", "banana", "cherry"]
my_list.extend(tropical)
print(type(my_list))
print(len(my_list))
print(my_list)

this_list.clear()
print(this_list)

# reversing a sorted list in descending order

thisList = ["orange", "mango", "kiwi", "pineapple", "banana"]
thisList.sort(reverse = True)
print(thisList)

user_input = input("Enter a number: ")

if user_input.isdigit():
    num = int(user_input)
    print("Valid input:", num)
else:
    print("Invalid number entered.")
while True:
    age = input("Enter your age: ")
    if age.isdigit():
        age = int(age)
        break
    else:
        print("Please enter a valid number.")
