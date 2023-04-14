def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

while True:
    year = input("연도를 입력하세요(종료: q): ")
    if year.lower() == "q":
        break
    try:
        year = int(year)
        if is_leap_year(year):
            print(f"{year}년은 윤년입니다.")
        else:
            print(f"{year}년은 평년입니다.")
    except ValueError:
        print("입력한 값이 올바른 연도가 아닙니다.")
