def Size(self):
    return s.uint32 + 12 + s.uint32 + s.uint32 + len(self.Payload)