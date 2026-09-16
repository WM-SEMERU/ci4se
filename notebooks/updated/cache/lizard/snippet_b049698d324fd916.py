def ringscan(x0, y0, r1, r2, metric=chebyshev):
    if r1 < 0:
        raise ValueError('Initial radius must be non-negative')
    if r2 < 0:
        raise ValueError('Final radius must be non-negative')
    if not hasattr(metric, '__call__'):
        raise TypeError('Metric not callable')
    direction = 0
    steps = {(0): [1, 0], (1): [1, -1], (2): [0, -1], (3): [-1, -1], (4): [
        -1, 0], (5): [-1, 1], (6): [0, 1], (7): [1, 1]}
    nsteps = len(steps)
    center = [x0, y0]
    rstep = 1 if r2 >= r1 else -1
    for distance in range(r1, r2 + rstep, rstep):
        initial = [x0, y0 + distance]
        current = initial
        ntrys = 0
        while True:
            if distance == 0:
                yield current[0], current[1]
                break
            nextpoint = [(current[i] + steps[direction][i]) for i in range(2)]
            if metric(center, nextpoint) != distance:
                ntrys += 1
                if ntrys == nsteps:
                    break
                direction = (direction + 1) % nsteps
                continue
            ntrys = 0
            yield current[0], current[1]
            current = nextpoint
            if current == initial:
                break
        if ntrys == nsteps:
            break