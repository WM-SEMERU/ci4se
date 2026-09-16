def chain_frames(self):
    prev_tb = None
    for tb in self.frames:
        if prev_tb is not None:
            prev_tb.tb_next = tb
        prev_tb = tb
    prev_tb.tb_next = None