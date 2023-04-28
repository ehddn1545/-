scores = []

for i in range(3):
    score = int(input(f"#{i+1}? "))
    scores.append(score)

average = sum(scores) / len(scores)

print("점수 출력")
print("입력 점수:", end=" ")
for score in scores:
    print(score, end=" ")

print("\n평균:", f"{average:.1f}")

search_score = int(input("검색할 점수는? "))
index = scores.index(search_score)

print(f"{search_score}점은 {index+1}번 학생의 점수입니다.")
