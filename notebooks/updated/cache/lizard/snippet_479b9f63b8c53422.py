def go_to_error(self, text):
    match = get_error_match(to_text_string(text))
    if match:
        fname, lnb = match.groups()
        self.edit_script(fname, int(lnb))