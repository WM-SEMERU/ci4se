def data(self, previous_data=False, prompt=False, console_row=False,
    console_row_to_cursor=False, console_row_from_cursor=False):
    result = ''
    if previous_data:
        result += self.__previous_data
    if prompt or console_row or console_row_to_cursor:
        result += self.console().prompt()
    if console_row or console_row_from_cursor and console_row_to_cursor:
        result += self.console().row()
    elif console_row_to_cursor:
        result += self.console().row()[:self.cursor()]
    elif console_row_from_cursor:
        result += self.console().row()[self.cursor():]
    return result