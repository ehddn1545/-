#구구단을 외우자
for a in range(2, 10):
    if a == 6:
        print()
    for b in range(1, 10):
        print(f'{a} x {b} = {a*b:2d}', end='\t')
        if b % 4 == 0:
            print()
