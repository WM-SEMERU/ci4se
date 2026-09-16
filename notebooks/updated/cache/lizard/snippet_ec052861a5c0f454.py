def getPiLambert(n):
    mypi = piGenLambert()
    result = []
    if n > 0:
        result += [next(mypi) for i in range(n)]
    mypi.close()
    return result