def iterator_from_slice(s):
    import numpy as np
    start = s.start if s.start is not None else 0
    step = s.step if s.step is not None else 1
    if s.stop is None:
        return itertools.count(start=start, step=step)
    else:
        return iter(np.arange(start, s.stop, step))