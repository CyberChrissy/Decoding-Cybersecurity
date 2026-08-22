Username = input("Enter your username: ")
Password = input("Enter your password: ")
attempts = int(input("Enter how many login attempts did you make: "))
if attempts >= 3:
    print("Access denied.")
elif attempts < 3: 
    print("Access granted.")
    