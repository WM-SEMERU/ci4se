def heaviest_increasing_subsequence(a, debug=False):
    L = {(0): -1}
    bestsofar = [(0, -1)] * len(a)
    for i, (key, weight) in enumerate(a):
        for w, j in L.items():
            if j != -1 and a[j][0] >= key:
                continue
            new_weight = w + weight
            if new_weight in L and a[L[new_weight]][0] <= key:
                continue
            L[new_weight] = i
            newbest = new_weight, j
            if newbest > bestsofar[i]:
                bestsofar[i] = newbest
        if debug:
            print((key, weight), bestsofar)
    tb = reversed(list(backtracking(a, L, bestsofar)))
    return [a[x] for x in tb], max(L.items())[0]