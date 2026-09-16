def sandwich_decompositions(coords0, coords1, samples=SAMPLES):
    decomps = []
    for _ in range(samples):
        circ = qf.Circuit()
        circ += qf.CANONICAL(*coords0, 0, 1)
        circ += qf.random_gate([0])
        circ += qf.random_gate([1])
        circ += qf.CANONICAL(*coords1, 0, 1)
        gate = circ.asgate()
        coords = qf.canonical_coords(gate)
        decomps.append(coords)
    return decomps