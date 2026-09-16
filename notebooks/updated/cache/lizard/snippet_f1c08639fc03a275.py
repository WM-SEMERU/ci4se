def adjust_bounding_box(bounds1, bounds2):
    if bounds2[0] > bounds1[0] and bounds2[2] > bounds1[0] or bounds2[2
        ] < bounds1[2] and bounds2[2] < bounds1[0]:
        return bounds1
    if bounds2[1] < bounds1[1] and bounds2[3] < bounds1[1] or bounds2[3
        ] > bounds1[3] and bounds2[1] > bounds1[3]:
        return bounds1
    new_bounds = list(bounds2)
    if bounds2[0] > bounds1[0] or bounds2[0] < bounds1[3]:
        new_bounds[0] = bounds1[0]
    if bounds2[2] < bounds1[2] or bounds2[2] > bounds1[0]:
        new_bounds[2] = bounds1[2]
    if bounds2[1] < bounds1[1] or bounds2[1] > bounds1[3]:
        new_bounds[1] = bounds1[1]
    if bounds2[3] > bounds1[3] or bounds2[3] < bounds1[1]:
        new_bounds[3] = bounds1[3]
    return tuple(new_bounds)