def generatePreKeys(start, count):
    results = []
    start -= 1
    for i in range(0, count):
        preKeyId = (start + i) % (Medium.MAX_VALUE - 1) + 1
        results.append(PreKeyRecord(preKeyId, Curve.generateKeyPair()))
    return results