def difference(self, other):
    diff = tuple(set(self.plates) - set(other.plates)), tuple(set(other.
        plates) - set(self.plates))
    counts = map(len, diff)
    is_sub_plate = counts == [1, 1] and diff[0][0].is_sub_plate(diff[1][0])
    if len(other.plates) == 1 and counts == [1, 0] and diff[0][0
        ].parent == other.plates[0].parent:
        is_sub_plate = True
    return diff, counts, is_sub_plate