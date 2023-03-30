Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
exchange_rate = None

def set_rate(won):
    global exchange_rate
    exchange_rate = 1 / won

def get_rate():
    return exchange_rate

def to_dollar(won):
    return won * exchange_rate

def to_won(dollar):
    return dollar / exchange_rate

def main():
    set_rate(int(input("$1에 대한 오늘의 환율은? ")))
    won_amount = int(input("원화로 변환할 달러화 액수는? "))
    dollar_amount = to_dollar(won_amount)
    print(f"{won_amount} 달러는 {dollar_amount} 원입니다")
    dollar_amount = int(input("달러화로 변환할 원화 액수는? "))
    won_amount = to_won(dollar_amount)
    print(f"{dollar_amount} 원은 {won_amount} 달러입니다")
