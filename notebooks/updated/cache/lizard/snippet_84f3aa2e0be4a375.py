def get_line_numbers(self, buffer):
    from_, to = self.operator_range(buffer.document)
    from_ += buffer.cursor_position
    to += buffer.cursor_position
    from_, _ = buffer.document.translate_index_to_position(from_)
    to, _ = buffer.document.translate_index_to_position(to)
    return from_, to