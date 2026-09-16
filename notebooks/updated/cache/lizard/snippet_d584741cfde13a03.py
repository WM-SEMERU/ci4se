def _calculateLrcString(inputstring):
    _checkString(inputstring, description='input LRC string')
    register = 0
    for character in inputstring:
        register += ord(character)
    lrc = (register ^ 255) + 1 & 255
    lrcString = _numToOneByteString(lrc)
    return lrcString