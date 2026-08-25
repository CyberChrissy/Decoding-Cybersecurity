# 
passwords = ["password1", "password2", "password3", "password4", "password5"]
for password in passwords:
    print(password)
#Dictionary are key value pairs
#Datebase is a dictionary that stores usernames and passwords
database = {"user1": "password1", "user2": "password2", "user3": "password3", "user4": "password4", "user5": "password5"}
for username, password in database.items():
    print(username, password)
# Investigating suspicious IP addresses
IP_addresses = ["192.168.1.10", "10.0.0.50", "172.16.0.25", "10.0.0.15", "56.90.100.5", "908.58.100.1", "809.90.100.5", "192.168.1.11"]
suspicious_IP_addresses = ["192.168.1.10", "10.0.0.50", "172.16.0.25","56.90.100.5"]
for ip_address in suspicious_IP_addresses:
    print("Investigating IP address:", ip_address)
ports = [21, 22, 80, 443]
print(ports)
for port in ports:
    print("checking port", port)
# while loops
count = 1
while count <= 5:
    print(count)
    count += 2
count = 1
while count < 10:
    print(count)
    if count == 5:
        print("break condition is met, exiting the loop")
        break
    count += 3
print("Loop has ended")
