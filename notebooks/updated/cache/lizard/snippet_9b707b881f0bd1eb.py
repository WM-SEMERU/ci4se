def first_blip(self, squash_axis, origin, initial_direction):
    from blmath.numerics import as_numeric_array
    origin = vx.reject_axis(as_numeric_array(origin, (3,)), axis=
        squash_axis, squash=True)
    initial_direction = vx.reject_axis(as_numeric_array(initial_direction,
        (3,)), axis=squash_axis, squash=True)
    vertices = vx.reject_axis(self.v, axis=squash_axis, squash=True)
    origin_to_mesh = vx.normalize(vertices - origin)
    cosines = vx.normalize(initial_direction).dot(origin_to_mesh.T).T
    index_of_first_blip = np.argmax(cosines)
    return self.v[index_of_first_blip]