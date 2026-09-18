correct_pin = "4321"
attempts = ["1111", "2222", "4321"]
index = 0

while True:
    entered_pin = attempts[index]
    print(f"Attempt {index + 1}: Entering PIN {entered_pin}")
    index +=1
    if entered_pin == correct_pin:
        print("PIN correct. Access granted")
        break
    else:
        print("Incorrect PIN. Try again")