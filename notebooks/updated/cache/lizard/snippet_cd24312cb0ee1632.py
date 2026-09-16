def from_lengths_and_angles(abc: List[float], ang: List[float]):
    return Lattice.from_parameters(abc[0], abc[1], abc[2], ang[0], ang[1],
        ang[2])