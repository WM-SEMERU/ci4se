def polynomial(target, a, prop, **kwargs):
    r
    x = target[prop]
    value = 0.0
    for i in range(0, len(a)):
        value += a[i] * x ** i
    return value