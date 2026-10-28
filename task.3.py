ids = ["T01", "T02", "T01", "T04"]
amounts = [300, 1500, 300, 800]
limit = 1000

check_1 = (ids[0] == ids[1]) or (ids[0] == ids[2]) or (ids[0] == ids[3]) or (amounts[0] > limit)
check_2 = (ids[1] == ids[0]) or (ids[1] == ids[2]) or (ids[1] == ids[3]) or (amounts[1] > limit)
check_3 = (ids[2] == ids[0]) or (ids[2] == ids[1]) or (ids[2] == ids[3]) or (amounts[2] > limit)
check_4 = (ids[3] == ids[0]) or (ids[3] == ids[1]) or (ids[3] == ids[2]) or (amounts[3] > limit)

print("Transaction IDs:", ids)
print("Amounts:", amounts)
print("Suspicious checks:", [check_1, check_2, check_3, check_4])