import os

def save_shopping_bag(filename, shopping_bag):
    with open(filename, 'w', encoding='utf-8') as file:
        for item in shopping_bag:
            file.write(item + '\n')

def load_shopping_bag(filename):
    shopping_bag = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                shopping_bag.append(line.strip())
    return shopping_bag

def display_shopping_bag(shopping_bag):
    print('장바구니 보기:', shopping_bag)

def main():
    filename = 'shoppingbag.txt'
    shopping_bag = load_shopping_bag(filename)

    while True:
        print('[구입]')
        item = input('상품명? ')
        if item:
            shopping_bag.append(item)
            print(f'장바구니에 {item}가(이) 담겼습니다.')
        else:
            display_shopping_bag(shopping_bag)
            save_shopping_bag(filename, shopping_bag)
            break

main()

