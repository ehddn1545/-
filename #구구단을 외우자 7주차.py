#구구단을 외우자
for i in range(2, 10):
    if i == 6:
        print()
    for j in range(1, 10):
        print(f'{i} x {j} = {i*j:2d}', end='\t')
        if j % 4 == 0:
            print()
