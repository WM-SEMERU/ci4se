def send(self, payload, opcode=ABNF.OPCODE_TEXT):
    frame = ABNF.create_frame(payload, opcode)
    return self.send_frame(frame)