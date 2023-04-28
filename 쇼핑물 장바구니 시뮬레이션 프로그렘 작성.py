shopping_bag = []

while True:
    item = input("상품명? ")
    if item == "더이상 살 물품이 없습니다" or item == "":
        break
    print(f"장바구니에 '{item}'가 담겼습니다.")
    shopping_bag.append(item)

print("장바구니 보기:", ", ".join(shopping_bag))