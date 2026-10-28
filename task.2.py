vehicle = input("Enter vehicle type (car/bike): ").lower()
entry_hour = int(input("Enter entry hour (0 to 23): "))
exit_hour = int(input("Enter exit hour (0 to 23): "))

rate = 30 * (vehicle == "car") + 15 * (vehicle == "bike")

hours = (exit_hour - entry_hour) % 24

fee = hours * rate

fee = min(fee, 300)

print("Parking hours:", hours)
print("Parking fee: ₹", fee)