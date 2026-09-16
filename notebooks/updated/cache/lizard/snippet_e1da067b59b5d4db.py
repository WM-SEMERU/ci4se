def popValue(self, argList):
    return self._Tuple(*[typeObj.popValue(argList) for name, typeObj in
        self._types.items()])