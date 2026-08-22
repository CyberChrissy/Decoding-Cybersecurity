Username = 'CyberChrissy'
Password = 'SecurePass123'
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    Input_username = input("Enter your username: ")
    Input_password = input("Enter your password: ")
    if Input_username == Username and Input_password == Password:
        print("Access granted") 
        break
    else:
        attempts += 1
        print("Incorrect login. Try again.")
        print(f"Attempt number:", attempts)
        if attempts >= max_attempts:
            print("Alert: Your account is locked due to multiple failed login attempts.")
