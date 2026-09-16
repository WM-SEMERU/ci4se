def dqdv_frames(cell, split=False, **kwargs):
    if split:
        return _dqdv_split_frames(cell, tidy=True, **kwargs)
    else:
        return _dqdv_combinded_frame(cell, **kwargs)