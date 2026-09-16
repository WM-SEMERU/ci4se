def print_message(self, message='heya!'):
    if self.log == None:
        print(message)
    else:
        self.log.append_text(message)