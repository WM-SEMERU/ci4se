def cross_entropy_calc(TOP, P, POP):
    try:
        result = 0
        for i in TOP.keys():
            reference_likelihood = P[i] / POP[i]
            response_likelihood = TOP[i] / POP[i]
            if response_likelihood != 0 and reference_likelihood != 0:
                result += reference_likelihood * math.log(response_likelihood,
                    2)
        return -result
    except Exception:
        return 'None'