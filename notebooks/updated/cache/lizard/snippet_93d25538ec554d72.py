def ShiftRight(x, **unused_kwargs):
    if not isinstance(x, (list, tuple)):
        pad_widths = [(0, 0), (1, 0)]
        padded = np.pad(x, pad_widths, mode='constant')
        return padded[:, :-1]
    padded = []
    last_value = np.zeros_like(x[0][:, (-1)])
    for chunk in x:
        padded_chunk = np.concatenate([last_value[:, (np.newaxis)], chunk],
            axis=1)
        last_value = chunk[:, (-1)]
        padded.append(padded_chunk[:, :-1])
    return padded