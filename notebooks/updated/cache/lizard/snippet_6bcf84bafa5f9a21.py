def RMSError(self):
    tss = self.TSSError()
    return math.sqrt(tss / self.size)