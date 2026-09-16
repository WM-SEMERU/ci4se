def td_sp(points, speed_threshold):
    if len(points) <= 2:
        return points
    else:
        max_speed_threshold = 0
        found_index = 0
        for i in range(1, len(points) - 1):
            dt1 = time_dist(points[i], points[i - 1])
            if dt1 == 0:
                dt1 = 1e-09
            vim = loc_dist(points[i], points[i - 1]) / dt1
            dt2 = time_dist(points[i + 1], points[i])
            if dt2 == 0:
                dt2 = 1e-09
            vi_ = loc_dist(points[i + 1], points[i]) / dt2
            if abs(vi_ - vim) > max_speed_threshold:
                max_speed_threshold = abs(vi_ - vim)
                found_index = i
        if max_speed_threshold > speed_threshold:
            one = td_sp(points[:found_index], speed_threshold)
            two = td_sp(points[found_index:], speed_threshold)
            one.extend(two)
            return one
        else:
            return [points[0], points[-1]]