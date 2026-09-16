def log_proto(self, proto, step_num):
    self.summ_writer.add_summary(proto, step_num)
    return proto