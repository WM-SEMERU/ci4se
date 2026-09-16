def confidence_level(self):
    z = self.z_score
    if isinstance(z, string_types):
        return z
    z = abs(round(z, 3))
    if z == 0.0:
        return 'No Change'
    elif z < 1.65:
        return 'No Confidence'
    elif z < 2.33:
        return '95% Confidence'
    elif z < 3.08:
        return '99% Confidence'
    return '99.9% Confidence'