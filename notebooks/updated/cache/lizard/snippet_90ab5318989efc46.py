def init(self, s):
    curses.curs_set(0)
    self.s = s
    self.s.keypad(1)
    self.set_screen_size()
    self.pads = {}
    self.offsets = {}
    self.init_help()
    self.init_streams_pad()
    self.current_pad = 'streams'
    self.set_title(TITLE_STRING)
    self.got_g = False
    signal.signal(28, self.resize)
    if self.config.CHECK_ONLINE_ON_START:
        self.check_online_streams()
    self.set_status('Ready')