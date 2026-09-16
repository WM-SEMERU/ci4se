def swo_num_bytes(self):
    res = self._dll.JLINKARM_SWO_Control(enums.JLinkSWOCommands.
        GET_NUM_BYTES, 0)
    if res < 0:
        raise errors.JLinkException(res)
    return res