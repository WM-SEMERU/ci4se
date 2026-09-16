def extract_features(points, n_tops):
    max_bin = -1
    for point in points:
        max_bin = max(max_bin, point.vel)
    max_bin = int(round(max_bin)) + 1
    histogram = [0] * max_bin
    time = 0
    for point in points:
        bin_index = int(round(point.vel))
        histogram[bin_index] += point.dt
        time += point.dt
    result = []
    if time == 0:
        return result
    for _ in range(n_tops):
        max_index = np.argmax(histogram)
        value = histogram[max_index] / time
        result.extend([max_index, value])
        histogram[max_index] = -1
    return result