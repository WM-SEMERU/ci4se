async def pin_6_pwm_128(my_board):
    await my_board.set_pin_mode(6, Constants.PWM)
    await my_board.analog_write(6, 128)
    await asyncio.sleep(3)
    await my_board.shutdown()