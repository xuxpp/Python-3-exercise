def fill_fibonacci(sequence, cnt):
    if cnt != 0:
        sequence.append(sequence[-1] + sequence[-2])
        fill_fibonacci(sequence, cnt-1)

def get_fibonacci(cnt):
    l = [0, 1]
    fill_fibonacci(l, cnt-2) # Deduct inital 2 numbers

    return l

print(get_fibonacci(21))