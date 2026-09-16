def blob_handler(self, cmd):
    self.blobs[cmd.id] = cmd
    self.keep = False