def prox_hard_plus(X, step, thresh=0):
    return prox_plus(prox_hard(X, step, thresh=thresh), step)