def list_data(self, previous_data=False, prompt=False, console_row=False,
    console_row_to_cursor=False, console_row_from_cursor=False):
    return self.split(self.data(previous_data, prompt, console_row,
        console_row_to_cursor, console_row_from_cursor))