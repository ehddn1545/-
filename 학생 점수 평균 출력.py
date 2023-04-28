scores = []

for i in range(3):
    score = int(input(f"#{i+1}? "))
    scores.append(score)

average = sum(scores) / len(scores)

print(scores)
print(f"평균: {average:.1f}")
