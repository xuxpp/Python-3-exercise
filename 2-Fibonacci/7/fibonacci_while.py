def get_fibonacci(cnt):
    l = [0, 1]

    while cnt - 2: # Deduct inital 2 numbers
        l.append(l[-1] + l[-2])
        cnt -= 1

    return l

print(get_fibonacci(21))