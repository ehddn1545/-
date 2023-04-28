shopping_bag = {}

while True:
    item = input("상품명? ")
    if item == "더이상 살 물품이 없습니다" or item == "":
        break
    quantity = int(input("수량은? "))
    shopping_bag[item] = quantity
    print(f"장바구니에 '{item}' {quantity}개가 담겼습니다.")

print("장바구니 보기:", end=" ")
for item, quantity in shopping_bag.items():
    print(f"{item}: {quantity}", end=", ")

search_item = input("\n장바구니에서 확인하고자 하는 상품은? ")
if search_item in shopping_bag:
    print(f"{search_item}은(는) {shopping_bag[search_item]}개 담겨 있습니다.")
else:
    print(f"{search_item}은(는) 담은적 없는 상품입니다.")
