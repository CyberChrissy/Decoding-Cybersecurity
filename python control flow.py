# Learning about if and else statements in Python
failed_attempts = 2
if failed_attempts >= 5:
    print("Warning: Multiple failed login attempts detected")    
else:
    print("Login successful")
percentage_score = 80
if percentage_score >= 90:
    print("Awarded a gold sticker")
else:
    print("Better luck next time")
"""
 Learning about comparison operators in Python
== (equal to)
!= (not equal to
<  (less than)
> (greater than)
<= (less than or equal to)
>= (greater than or equal to)
"""
print("Attempts == 5")
print("2 x 2 != 6")
print("80 < 90")
print("90 > 80")
print("percentage score <= 90 award gold sticker")
print("percentage score >= 89 better luck next time")

# Exercise 1: Write a program that asks the user how many failed login attemps occured. 
# If the number is 3 or more, display an alert indicating that the account is locked. 
# Otherwise display a message indicating that the account is still active.
# Solution to exercise 1

Username = 'CyberChrissy'
Password = 'SecurePass123'
Input_username = input("Enter your username: ")
Input_password = input("Enter your password: ")
if Input_username == Username and Input_password == Password:
    print("Access granted") 
else: print ("Your account is still active. Please try again.")
repeat_attempts = 1
if repeat_attempts >= 3:
    print("Alert: Your account is locked due to multiple failed login attempts.")

failed_attempts = int(input("How many failed login attempts occurred? "))

if failed_attempts >= 3:
    print("Alert: Your account is locked due to multiple failed login attempts.")
          
# Elif statements in Python (multiple conditions)
failed_attempts = int(input("How many failed login attempts occurred? "))
if failed_attempts >= 10:
    print("critical alert!")
elif failed_attempts >= 5:
    print("Warning!")
else:
    print("normal")

# Exercise 2: Write a program that requests the username, password and number of failed attempts of the user.
# Then use conditions to determine whether access is granted or not.
