def cost(a, b, c, e, f, p_min, p):
    return a + b * p + c * p * p + abs(e * math.sin(f * (p_min - p)))