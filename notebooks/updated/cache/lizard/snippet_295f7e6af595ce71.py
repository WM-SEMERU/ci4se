def _validate_frequency(cls, index, freq, **kwargs):
    if is_period_dtype(cls):
        return None
    inferred = index.inferred_freq
    if index.size == 0 or inferred == freq.freqstr:
        return None
    try:
        on_freq = cls._generate_range(start=index[0], end=None, periods=len
            (index), freq=freq, **kwargs)
        if not np.array_equal(index.asi8, on_freq.asi8):
            raise ValueError
    except ValueError as e:
        if 'non-fixed' in str(e):
            raise e
        raise ValueError(
            'Inferred frequency {infer} from passed values does not conform to passed frequency {passed}'
            .format(infer=inferred, passed=freq.freqstr))