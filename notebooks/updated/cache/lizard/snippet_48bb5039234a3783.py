def index_of_nearest(p, hot_points, distance_f=distance):
    min_dist = None
    nearest_hp_i = None
    for i, hp in enumerate(hot_points):
        dist = distance_f(p, hp)
        if min_dist is None or dist < min_dist:
            min_dist = dist
            nearest_hp_i = i
    return nearest_hp_i