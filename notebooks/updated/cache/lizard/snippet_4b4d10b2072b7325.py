def _calculateCrcString(inputstring):
    _checkString(inputstring, description='input CRC string')
    register = 65535
    for char in inputstring:
        register = register >> 8 ^ _CRC16TABLE[(register ^ ord(char)) & 255]
    return _numToTwoByteString(register, LsbFirst=True)