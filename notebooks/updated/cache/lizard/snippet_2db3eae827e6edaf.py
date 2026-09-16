def GetStructByteOrderString(self):
    if not self._data_type_definition:
        return None
    return self._BYTE_ORDER_STRINGS.get(self._data_type_definition.
        byte_order, None)