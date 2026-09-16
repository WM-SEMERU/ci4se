def percent_pareto_recharges(recharges, percentage=0.8):
    amounts = sorted([r.amount for r in recharges], reverse=True)
    total_sum = sum(amounts)
    partial_sum = 0
    for count, a in enumerate(amounts):
        partial_sum += a
        if partial_sum >= percentage * total_sum:
            break
    return (count + 1) / len(recharges)