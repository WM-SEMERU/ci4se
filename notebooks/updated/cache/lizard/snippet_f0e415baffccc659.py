def get_full_command(self):
    if self.is_command():
        command, _, args = self.text.partition(' ')
        return command, args