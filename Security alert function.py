def check_login_attempts(attempts):
    if attempts >= 10:
        return "critical"
    elif attempts >= 5:
        return "warning"
    else:
        return "normal"
print(check_login_attempts(2))
print(check_login_attempts(7))
print(check_login_attempts(15))
