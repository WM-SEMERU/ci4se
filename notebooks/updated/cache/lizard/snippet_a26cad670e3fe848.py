def positive_volume_index(close_data, volume):
    catch_errors.check_for_input_len_diff(close_data, volume)
    pvi = np.zeros(len(volume))
    pvi[0] = 1
    for idx in range(1, len(volume)):
        if volume[idx] > volume[idx - 1]:
            pvi[idx] = volume_index_helper(pvi, idx, close_data)
        else:
            pvi[idx] = pvi[idx - 1]
    return pvi