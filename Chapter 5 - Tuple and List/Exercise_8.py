scores = []
print("Enter the scores for the test. Use -1 if you want to finish")
score = float(input("Score: "))

while score != -1:
    scores.append(score)
    score = float(input("Score: "))

print("The scores (ordered):", sorted(scores))

print("The average of these", len(scores), "scores =", round(sum(scores) / len(scores), 2))
