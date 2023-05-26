from datetime import datetime

class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

def get_current_time():
    now = datetime.now()
    return Time(now.hour, now.minute)

def save_time(time):
    with open('last.dat', 'w') as file:
        file.write(f'{time.hour}:{time.minute}')

def load_time():
    with open('last.dat', 'r') as file:
        time_str = file.read()
        hour, minute = time_str.split(':')
        return Time(int(hour), int(minute))

def main():
    try:
        last_time = load_time()
        print(f'안녕하세요, 마지막으로 {last_time.hour:02d}:{last_time.minute:02d}에 실행되었습니다.')
    except FileNotFoundError:
        print('안녕하세요, 처음 실행되었습니다.')

    current_time = get_current_time()
    print(f'지금은 {current_time.hour:02d}:{current_time.minute:02d} 입니다.')

    last_time = current_time
    save_time(last_time)

main()
