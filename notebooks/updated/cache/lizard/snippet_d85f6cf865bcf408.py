def send_message(self, message):
    self.print_debug_message(message)
    self.socket.send(message)