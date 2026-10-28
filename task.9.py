available_books = 12

branch_a_need = 8
branch_b_need = 7

branch_a_books = 6
branch_b_books = available_books - branch_a_books

branch_a_unmet = branch_a_need - branch_a_books
branch_b_unmet = branch_b_need - branch_b_books

print("Branch A receives:", branch_a_books)
print("Branch A still needs:", branch_a_unmet)
print("Branch B receives:", branch_b_books)
print("Branch B still needs:", branch_b_unmet)