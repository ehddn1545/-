def print_file_contents(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i, line in enumerate(lines, 1):
            print(f'{i}: {line.strip()}')

# 텍스트 파일의 경로와 이름을 입력하세요
filename = 'readme.txt'

print_file_contents(filename)
