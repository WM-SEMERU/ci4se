def normalizeRotationAngle(value):
    if not isinstance(value, (int, float)):
        raise TypeError(
            'Angle must be instances of :ref:`type-int-float`, not %s.' %
            type(value).__name__)
    if abs(value) > 360:
        raise ValueError('Angle must be between -360 and 360.')
    if value < 0:
        value = value + 360
    return float(value)