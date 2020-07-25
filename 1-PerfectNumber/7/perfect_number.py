def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0: sum += i

    return sum == n

r = int(input("Give range: "))

for i in range(1, r):
    if is_perfect(i):
        print(i)