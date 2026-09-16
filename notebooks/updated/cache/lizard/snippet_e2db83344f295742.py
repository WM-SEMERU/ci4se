def right_brake(self):
    self.board.digital_write(R_CTRL_1, 1)
    self.board.digital_write(R_CTRL_2, 1)
    self.board.analog_write(PWM_R, 0)