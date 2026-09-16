async def set_ch_enable_bit(self, ch_bit, timeout=OTGW_DEFAULT_TIMEOUT):
    if ch_bit not in [0, 1]:
        return None
    cmd = OTGW_CMD_CONTROL_HEATING
    status = {}
    ret = await self._wait_for_cmd(cmd, ch_bit, timeout)
    if ret is None:
        return
    ret = int(ret)
    status[DATA_MASTER_CH_ENABLED] = ret
    self._update_status(status)
    return ret