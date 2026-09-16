def buying_pressure(close_data, low_data):
    catch_errors.check_for_input_len_diff(close_data, low_data)
    bp = [(close_data[idx] - np.min([low_data[idx], close_data[idx - 1]])) for
        idx in range(1, len(close_data))]
    bp = fill_for_noncomputable_vals(close_data, bp)
    return bp