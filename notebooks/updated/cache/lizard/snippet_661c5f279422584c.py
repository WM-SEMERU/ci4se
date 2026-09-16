def split_bodies(dataset, label=False):
    labeled = dataset.connectivity()
    classifier = labeled.cell_arrays['RegionId']
    bodies = vtki.MultiBlock()
    for vid in np.unique(classifier):
        b = labeled.threshold([vid - 0.5, vid + 0.5], scalars='RegionId')
        if not label:
            b._remove_cell_scalar('RegionId')
            b._remove_point_scalar('RegionId')
        bodies.append(b)
    return bodies