def prepare(self, inputstring, strip=False, nl_at_eof_check=False, **kwargs):
    if (self.strict and nl_at_eof_check and inputstring and not inputstring
        .endswith('\n')):
        end_index = len(inputstring) - 1 if inputstring else 0
        raise self.make_err(CoconutStyleError,
            'missing new line at end of file', inputstring, end_index)
    original_lines = inputstring.splitlines()
    if self.keep_lines:
        self.original_lines = original_lines
    inputstring = '\n'.join(original_lines)
    if strip:
        inputstring = inputstring.strip()
    return inputstring