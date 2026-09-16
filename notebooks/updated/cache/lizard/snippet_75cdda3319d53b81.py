def entropy(s):
    return -sum(p * np.log(p) for i in range(len(s)) for p in [prop(s[i], s)])