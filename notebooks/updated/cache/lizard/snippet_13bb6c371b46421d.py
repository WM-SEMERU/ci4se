def check_split_ratio(split_ratio):
    valid_ratio = 0.0
    if isinstance(split_ratio, float):
        assert 0.0 < split_ratio < 1.0, 'Split ratio {} not between 0 and 1'.format(
            split_ratio)
        test_ratio = 1.0 - split_ratio
        return split_ratio, test_ratio, valid_ratio
    elif isinstance(split_ratio, list):
        length = len(split_ratio)
        assert length == 2 or length == 3, 'Length of split ratio list should be 2 or 3, got {}'.format(
            split_ratio)
        ratio_sum = sum(split_ratio)
        if not ratio_sum == 1.0:
            split_ratio = [(float(ratio) / ratio_sum) for ratio in split_ratio]
        if length == 2:
            return tuple(split_ratio + [valid_ratio])
        return tuple(split_ratio)
    else:
        raise ValueError('Split ratio must be float or a list, got {}'.
            format(type(split_ratio)))