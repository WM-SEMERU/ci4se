def speed_difference(points):
    data = [0]
    for before, after in pairwise(points):
        data.append(before.vel - after.vel)
    return data