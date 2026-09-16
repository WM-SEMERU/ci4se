def set_out(self, que_out, num_followers):
    for p in self.processes:
        p.set_out(que_out, num_followers)