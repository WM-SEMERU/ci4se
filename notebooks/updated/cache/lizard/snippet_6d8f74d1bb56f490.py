def bufferoutput(self):
    new_stream = Stream(writebufferlimit=None)
    if self._sendHeaders:
        self.container.subroutine(new_stream.copy_to(self.outputstream,
            self.container, buffering=False))
    self.outputstream = Stream(writebufferlimit=None)