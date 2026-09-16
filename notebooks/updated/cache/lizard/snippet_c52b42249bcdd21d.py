def read_bit(self, registeraddress, functioncode=2):
    _checkFunctioncode(functioncode, [1, 2])
    return self._genericCommand(functioncode, registeraddress)