def add_tuning(instrument, description, tuning):
    t = StringTuning(instrument, description, tuning)
    if _known.has_key(str.upper(instrument)):
        _known[str.upper(instrument)][1][str.upper(description)] = t
    else:
        _known[str.upper(instrument)] = instrument, {str.upper(description): t}