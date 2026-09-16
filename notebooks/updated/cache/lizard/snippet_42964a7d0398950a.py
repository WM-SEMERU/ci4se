def local_error(self, originalValue, calculatedValue):
    originalValue = originalValue[0]
    calculatedValue = calculatedValue[0]
    if 0 == originalValue:
        return None
    return math.fabs((calculatedValue - originalValue) / float(originalValue)
        ) * 100.0