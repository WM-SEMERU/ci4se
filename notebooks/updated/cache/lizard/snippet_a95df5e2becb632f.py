def transform(self, v3):
    if isinstance(v3, Vector3):
        t = super(Quaternion, self).transform([v3.x, v3.y, v3.z])
        return Vector3(t[0], t[1], t[2])
    elif len(v3) == 3:
        return super(Quaternion, self).transform(v3)
    else:
        raise TypeError('param v3 is not a vector type')