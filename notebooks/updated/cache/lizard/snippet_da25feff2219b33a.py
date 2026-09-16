def count_selfintersections(self):
    counter = 0
    for i, j in itertools.combinations(range(len(self.lineSegments)), 2):
        inters = get_segments_intersections(self.lineSegments[i], self.
            lineSegments[j])
        if abs(i - j) > 1 and len(inters) > 0:
            counter += 1
    return counter