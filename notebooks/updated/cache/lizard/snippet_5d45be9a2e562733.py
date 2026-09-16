def edit_content(self, original_lines, file_name):
    lines = [self.edit_line(line) for line in original_lines]
    for function in self._functions:
        try:
            lines = list(function(lines, file_name))
        except UnicodeDecodeError as err:
            log.error('failed to process %s: %s', file_name, err)
            return lines
        except Exception as err:
            log.error('failed to process %s with code %s: %s', file_name,
                function, err)
            raise
    return lines