def complete(self, flag_message='Complete', padding=None, force=False):
    if self.should_log(self.COMPLETE) or force:
        self._print_message(flag_message=flag_message, color=colors.
            complete_color, padding=padding)