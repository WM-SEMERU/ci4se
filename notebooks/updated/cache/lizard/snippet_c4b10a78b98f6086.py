def vietes(coefficients):
    r
    elementary_symmetric_polynomial = []
    tail = float(coefficients[-1])
    size = len(coefficients)
    for i in range(size):
        sign = 1 if i % 2 == 0 else -1
        el = sign * coefficients[size - i - 1] / tail
        elementary_symmetric_polynomial.append(el)
    return elementary_symmetric_polynomial