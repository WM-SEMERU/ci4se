def eol_distance_next(self, offset=0):
    distance = 0
    for char in self.string[self.pos + offset:]:
        if char == '\n':
            break
        else:
            distance += 1
    return distance