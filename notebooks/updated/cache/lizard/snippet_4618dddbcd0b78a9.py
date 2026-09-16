async def read_tap(self, callback=None):
    register = self.MMA8452Q_Register['PULSE_SRC']
    await self.board.i2c_read_request(self.address, register, 1, Constants.
        I2C_READ | Constants.I2C_END_TX_MASK, self.data_val, Constants.
        CB_TYPE_ASYNCIO)
    tap_status = await self.wait_for_read_result()
    tap_status = tap_status[self.data_start]
    if tap_status & 128:
        tap_status &= 127
    else:
        tap_status = 0
    if callback:
        await callback(tap_status)
    await asyncio.sleep(0.001)
    return tap_status