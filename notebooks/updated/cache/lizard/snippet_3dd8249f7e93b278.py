def unit(self, name: Optional[UnitName]=None, symbol=False):
    result = self._validate_enum(item=name, enum=UnitName)
    if symbol:
        return result[1]
    return result[0]