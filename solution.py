def sum_multiples(multiples, limit):
    s = 0
    for m in multiples:
        s += sum(range(m, limit, m))
    return s

result = sum_multiples([3,5], 1000)
print(result)

