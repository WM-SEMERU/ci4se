def month_indices(months):
    if not isinstance(months, (int, str)):
        raise TypeError(
            '`months` must be of type int or str: type(months) == {}'.
            format(type(months)))
    if isinstance(months, int):
        return [months]
    if months.lower() == 'ann':
        return np.arange(1, 13)
    first_letter = 'jfmamjjasond' * 2
    count = first_letter.count(months)
    if count == 0 or count > 2:
        message = (
            "The user must provide a unique pattern of consecutive first letters of months within '{}'. The provided string '{}' does not comply.  For individual months use integers."
            .format(first_letter, months))
        raise ValueError(message)
    st_ind = first_letter.find(months.lower())
    return np.arange(st_ind, st_ind + len(months)) % 12 + 1