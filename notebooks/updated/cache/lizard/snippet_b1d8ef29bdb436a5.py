def hailstone(n):
    sequence = [n]
    while n > 1:
        if n % 2 != 0:
            n = 3 * n + 1
        else:
            n = int(n / 2)
        sequence.append(n)
    return sequence