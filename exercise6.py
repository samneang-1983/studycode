seats_available = 5
seat_number = 1
while seats_available > 0:
    print(f"Selling ticket for seat {seat_number}")
    seats_available -= 1
    seat_number += 1
print("All tickets sold out!")