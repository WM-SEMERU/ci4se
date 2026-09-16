def set_led(self, led, action=None, cabinet=Required, frame=Required, board
    =Required):
    if isinstance(led, int):
        leds = [led]
    else:
        leds = led
    if isinstance(board, int):
        boards = [board]
    else:
        boards = list(board)
        board = boards[0]
    arg1 = sum(LEDAction.from_bool(action) << led * 2 for led in leds)
    arg2 = sum(1 << b for b in boards)
    self._send_scp(cabinet, frame, board, SCPCommands.led, arg1=arg1, arg2=
        arg2, expected_args=0)