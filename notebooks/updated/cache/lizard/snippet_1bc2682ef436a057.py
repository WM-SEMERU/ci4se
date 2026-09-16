def pin_6_pwm_128():
    board = PyMata3()
    board.set_pin_mode(6, Constants.PWM)
    board.analog_write(6, 128)
    board.sleep(3)
    board.shutdown()