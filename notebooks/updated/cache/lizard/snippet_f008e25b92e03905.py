def init_signal(self):
    self.signal = Signal()
    self.signal.set(feeder_exited=False, parser_exited=False, reach_max_num
        =False)