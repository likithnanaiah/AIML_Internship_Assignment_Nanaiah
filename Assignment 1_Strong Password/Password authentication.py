# Stored password
correct_password = "Strong123"

# Allow 3 attempts
attempts = 3

while attempts > 0:
    user_password = input("Enter password: ")

    if user_password == correct_password:
        print("Access Granted")
        break
    else:
        attempts -= 1
        print("Wrong password. Attempts left:", attempts)

if attempts == 0:
    print("Access Denied")