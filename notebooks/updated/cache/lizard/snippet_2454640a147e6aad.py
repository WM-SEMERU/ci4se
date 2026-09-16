def bin_annotation(annotation=None, subsampling_factor=3):
    if annotation is None:
        annotation = np.array([])
    n = len(annotation)
    binned_positions = [annotation[i] for i in range(n) if i %
        subsampling_factor == 0]
    if len(binned_positions) == 0:
        binned_positions.append(0)
    return np.array(binned_positions)