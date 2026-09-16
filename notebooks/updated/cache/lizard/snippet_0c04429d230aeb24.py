def interpolate(self, target, extent):
    target = cast_anything_to_vector(target)
    self += extent * (target - self)