def get_fibonaccis(cnt):
    l = [0, 1]
    
    for _ in range(cnt-2): # Deduct inital 2 numbers
        l.append(l[-1] + l[-2])

    return l

def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0: sum += i

    return sum == n

def get_non_perfect_nums(cnt):
    l = []
    n = 1
    while len(l) != cnt:
        if not is_perfect(n):
            l.append(n)
        n += 1
    return l

# Start of the execution
length = 21
l = []

l.append(get_non_perfect_nums(length))
l.append(get_fibonaccis(length))

tmp_list = []
for n1, n2 in zip(l[0], l[1]):
    tmp_list.append(n1 * n2)

l.append(tmp_list)

print(l)