Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import exchange_currency

def main():
    won_rate = float(input("전일 환율을 입력하세요: "))
    exchange_currency.set_rate(won_rate)

    dollar = float(input("원화로 변환할 달러화 액수를 입력하세요: "))
    won = exchange_currency.to_won(dollar)
    print(f"{dollar} 달러는 {won} 원입니다.")

    won = float(input("달러화로 변환할 원화 액수를 입력하세요: "))
    dollar = exchange_currency.to_dollar(won)
    print(f"{won} 원은 {dollar} 달러입니다.")

if __name__ == "__main__":
    main()
