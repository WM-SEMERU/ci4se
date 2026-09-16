def soln2point(soln, litmap):
    return {litmap[i]: int(val > 0) for i, val in enumerate(soln, start=1)}