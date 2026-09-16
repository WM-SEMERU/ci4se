def find(self, node, interval, start, end):
    data = []
    if len(interval) != 2:
        raise SyntaxError(
            'Interval malformed %s. Allways specify start and end position for interval.'
             % str(interval))
    left = start, node[0]
    right = node[0], end
    if self.overlap(left, interval):
        data.extend(node[-1])
        if node[1] != -1:
            data.extend(self.find(node[1], interval, left[0], left[1]))
    if self.overlap(right, interval):
        data.extend(node[-1])
        if node[2] != -1:
            data.extend(self.find(node[2], interval, right[0], right[1]))
    return list(set(data))