def money_flow(close_data, high_data, low_data, volume):
    catch_errors.check_for_input_len_diff(close_data, high_data, low_data,
        volume)
    mf = volume * tp(close_data, high_data, low_data)
    return mf