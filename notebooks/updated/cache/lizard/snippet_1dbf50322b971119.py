def log_ncr(a, b):
    val = gammaln(a + 1) - gammaln(a - b + 1) - gammaln(b + 1)
    return val