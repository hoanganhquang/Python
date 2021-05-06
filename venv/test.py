def add(*agr):
    total = 0
    for i in agr:
        total += i
    return total

print(add(1, 2, 3))