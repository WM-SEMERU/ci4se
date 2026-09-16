def stop_program(self, turn_off_load=True):
    self.__set_buffer_start(self.CMD_STOP_PROG)
    self.__set_checksum()
    self.__send_buffer()
    if turn_off_load and self.load_on:
        self.load_on = False