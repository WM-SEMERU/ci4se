def negative_volume_index(close_data, volume):
    catch_errors.check_for_input_len_diff(close_data, volume)
    nvi = np.zeros(len(volume))
    nvi[0] = 1
    for idx in range(1, len(volume)):
        if volume[idx] < volume[idx - 1]:
            nvi[idx] = volume_index_helper(nvi, idx, close_data)
        else:
            nvi[idx] = nvi[idx - 1]
    return nvi