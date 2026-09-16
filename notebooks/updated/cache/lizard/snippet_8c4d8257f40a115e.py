def decrypt(self, ciphertext):
    enc_key = ciphertext[:3]
    message = ciphertext[3:-3]
    grundstellung = ciphertext[-3:]
    self.machine.set_display(grundstellung)
    msg_key = self.machine.process_text(enc_key)
    self.machine.set_display(msg_key)
    return self.machine.process_text(message)