n = list(map(int, input().split()))
tn = set()
for num in n:
    if num in tn:
        print('YES')
    else:
        print('NO')
    tn.add(num)
