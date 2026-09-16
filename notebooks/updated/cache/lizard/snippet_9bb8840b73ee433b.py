def last_timestamp(self, sid, epoch=False):
    timestamp, value = self.last_datapoint(sid, epoch)
    return timestamp