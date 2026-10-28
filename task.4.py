feedback = input("Enter student feedback: ").lower()

positive_count = feedback.count("good") + feedback.count("helpful")
negative_count = feedback.count("bad") + feedback.count("boring")

score = positive_count - negative_count

print("Positive words:", positive_count)
print("Negative words:", negative_count)
print("Score:", score)