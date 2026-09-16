def cpe_equal(cls, source, target):
    for att, result in CPESet2_3.compare_wfns(source, target):
        isEqual = result == CPESet2_3.LOGICAL_VALUE_EQUAL
        if not isEqual:
            return False
    return True