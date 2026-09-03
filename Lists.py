count = 1
while count < 10:
    print(count)
    if count == 5:
        print("break condition is met, exiting the loop")
        break
    count += 3
print("Loop has ended")
#exercise 3: write a program that asks user to enter a password then classify as weak, moderate or strong

username = input("Enter your username: ")
password = input("Enter your password: ")
has_special_character = any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password)
if len(password) < 6 or not has_special_character:
    print("Weak password")
elif len(password) <= 10 and has_special_character:
    print("Moderate password")
else:
    print("Strong password")
