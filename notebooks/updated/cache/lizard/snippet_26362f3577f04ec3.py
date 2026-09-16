def lfriedmanchisquare(*args):
    k = len(args)
    if k < 3:
        raise ValueError('Less than 3 levels.  Friedman test not appropriate.')
    n = len(args[0])
    data = pstat.abut(*tuple(args))
    for i in range(len(data)):
        data[i] = rankdata(data[i])
    ssbn = 0
    for i in range(k):
        ssbn = ssbn + sum(args[i]) ** 2
    chisq = 12.0 / (k * n * (k + 1)) * ssbn - 3 * n * (k + 1)
    return chisq, chisqprob(chisq, k - 1)