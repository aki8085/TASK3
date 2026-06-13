PASSWORD = "Aki181224"
max_attempts = 3

for attempt in range(1, max_attempts + 1):
    entered = input(f"Attempt {attempt} - Enter password: ")
    if entered == PASSWORD:
        print("Access Granted")
        break
    else:
        remaining = max_attempts - attempt
        if remaining > 0:
            print(f"Wrong password! {remaining} attempt(s) left.")
else:
    print("Account Locked")
