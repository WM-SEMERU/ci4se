def shapes(self):
    if self._shapes:
        return self._shapes
    self.log('Generating shapes...')
    ret = collections.defaultdict(entities.ShapeLine)
    for point in self.read('shapes'):
        ret[point['shape_id']].add_child(point)
    self._shapes = ret
    return self._shapes