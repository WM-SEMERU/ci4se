def account_distance(A1, A2):
    return sum([action.alpha for action in A1]) - sum([action.alpha for
        action in A2])