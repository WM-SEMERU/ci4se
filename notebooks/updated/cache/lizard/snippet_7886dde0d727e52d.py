def accounting_sample_replace(total, data, accounting_column, prob_column=
    None, max_iterations=50):
    p = get_probs(data, prob_column)
    per_sample = data[accounting_column].sum() / (1.0 * len(data.index.values))
    curr_total = 0
    remaining = total
    sample_rows = pd.DataFrame()
    closest = None
    closest_remain = total
    matched = False
    for i in range(0, max_iterations):
        if remaining == 0:
            matched = True
            break
        if p is not None and i == 1:
            per_sample = sample_rows[accounting_column].sum() / (1.0 * len(
                sample_rows))
        num_samples = int(math.ceil(math.fabs(remaining) / per_sample))
        if remaining > 0:
            curr_ids = np.random.choice(data.index.values, num_samples, p=p)
            sample_rows = pd.concat([sample_rows, data.loc[curr_ids]])
        else:
            sample_rows = sample_rows.iloc[num_samples:].copy()
        curr_total = sample_rows[accounting_column].sum()
        remaining = total - curr_total
        if abs(remaining) < closest_remain:
            closest_remain = abs(remaining)
            closest = sample_rows
    return closest, matched