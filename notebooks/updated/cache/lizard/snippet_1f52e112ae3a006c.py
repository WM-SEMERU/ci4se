def success(self):
    return self.ack.upper() in (self.config.ACK_SUCCESS, self.config.
        ACK_SUCCESS_WITH_WARNING)