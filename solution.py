def fibonnacci():
    prev = [0, 1]
    while(True):
        n = sum(prev)
        prev[0] = prev[1]
        prev[1] = n
        yield n

s = 0

for fib in fibonnacci():
    if fib < 4000000:
        if fib % 2 == 0:
            s += fib
    else:
        break

print(s)