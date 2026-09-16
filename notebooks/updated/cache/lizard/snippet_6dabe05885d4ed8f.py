def set_log_channel(self, name):
    self.log_name = name
    self.logger = util.get_logger(name)
    self.packetizer.set_log(self.logger)