def cross(r1, r2):
    if r1.size != r2.size:
        raise ValueError('Both arguments must have the same input size.')
    if r1.deriv != r2.deriv:
        raise ValueError('Both arguments must have the same deriv.')
    result = Vector3(r1.size, r1.deriv)
    result.x = r1.y * r2.z - r1.z * r2.y
    result.y = r1.z * r2.x - r1.x * r2.z
    result.z = r1.x * r2.y - r1.y * r2.x
    return result