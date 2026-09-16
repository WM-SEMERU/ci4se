def compute_agreement_score(num_matches, num1, num2):
    denom = num1 + num2 - num_matches
    if denom == 0:
        return 0
    return num_matches / denom