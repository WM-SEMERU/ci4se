def percent_k(data, period):
    catch_errors.check_for_period_error(data, period)
    percent_k = [((data[idx] - np.min(data[idx + 1 - period:idx + 1])) / (
        np.max(data[idx + 1 - period:idx + 1]) - np.min(data[idx + 1 -
        period:idx + 1]))) for idx in range(period - 1, len(data))]
    percent_k = fill_for_noncomputable_vals(data, percent_k)
    return percent_k