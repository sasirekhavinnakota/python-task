distance = float(input("Enter journey distance in km: "))
age = int(input("Enter passenger age: "))

print("Choose travel class:")
print("1. Sleeper")
print("2. AC 3 Tier")
print("3. AC 2 Tier")
choice = input("Enter 1, 2, or 3: ")

rate = 1
class_name = "Sleeper"

choice == "2" and (rate := 2, class_name := "AC 3 Tier")
choice == "3" and (rate := 3, class_name := "AC 2 Tier")

fare = distance * rate

# Apply an age concession
concession = 0
age >= 60 and (concession := 0.40)
age < 12 and (concession := 0.50)

fare = fare - (fare * concession)

reservation_fee = 40
total_fare = fare + reservation_fee

print("Class:", class_name)
print("Fare after concession: ₹", round(fare, 2))
print("Reservation fee: ₹", reservation_fee)
print("Total fare: ₹", round(total_fare, 2))

cancel = input("Cancel reservation? (yes/no): ")
penalty = 100 * (cancel == "yes")
refund = total_fare - penalty

print("Cancellation penalty: ₹", penalty)
print("Refund: ₹", round(refund, 2))