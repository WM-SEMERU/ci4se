def getAnalogActionData(self, action, unActionDataSize, ulRestrictToDevice):
    fn = self.function_table.getAnalogActionData
    pActionData = InputAnalogActionData_t()
    result = fn(action, byref(pActionData), unActionDataSize,
        ulRestrictToDevice)
    return result, pActionData