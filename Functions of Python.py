def calculate_failure_rate(total_attempts, failed_attempts):
    return (failed_attempts / total_attempts) * 100

total_attempts = int(input("Enter total login attmept:"))
failed_attempts = int(input("Enter failed_attempts:"))
failure_rate = int(calculate_failure_rate(total_attempts, failed_attempts)) 
print("failure rate is:", failure_rate, "%")
