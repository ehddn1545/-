# 나이를 입력받는 함수
def input_age(prompt):
    while True:
        try:
            age = int(input(prompt))
            if 0 <= age <= 120:
                return age
            else:
                print("입력한 나이가 유효하지 않습니다. 다시 입력해주세요.")
        except ValueError:
            print("입력한 값이 올바른 숫자가 아닙니다. 다시 입력해주세요.")

# 성인 여부를 판별하는 함수
def is_adult(age):
    return age >= 19

# 주 프로그램
age = input_age("나이를 입력하세요: ")
if age == -1:
    print("입력한 나이가 유효하지 않습니다.")
else:
    if is_adult(age):
        print("성인입니다.")
    else:
        print("미성년자입니다.")
