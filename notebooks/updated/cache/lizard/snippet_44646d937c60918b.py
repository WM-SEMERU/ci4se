def gpio_set(self, pins, states):
    if len(pins) != len(states):
        raise ValueError('Length mismatch between pins and states.')
    size = len(pins)
    indices = (ctypes.c_uint8 * size)(*pins)
    states = (ctypes.c_uint8 * size)(*states)
    result_states = (ctypes.c_uint8 * size)()
    result = self._dll.JLINK_EMU_GPIO_SetState(ctypes.byref(indices),
        ctypes.byref(states), ctypes.byref(result_states), size)
    if result < 0:
        raise errors.JLinkException(result)
    return list(result_states)