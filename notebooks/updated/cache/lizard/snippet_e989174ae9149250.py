def strip_ansi_escape_codes(self, string_buffer):
    log.debug('In strip_ansi_escape_codes')
    log.debug('repr = {}'.format(repr(string_buffer)))
    code_position_cursor = chr(27) + '\\[\\d+;\\d+H'
    code_show_cursor = chr(27) + '\\[\\?25h'
    code_next_line = chr(27) + 'E'
    code_erase_line_end = chr(27) + '\\[K'
    code_erase_line = chr(27) + '\\[2K'
    code_erase_start_line = chr(27) + '\\[K'
    code_enable_scroll = chr(27) + '\\[\\d+;\\d+r'
    code_form_feed = chr(27) + '\\[1L'
    code_carriage_return = chr(27) + '\\[1M'
    code_disable_line_wrapping = chr(27) + '\\[\\?7l'
    code_reset_mode_screen_options = chr(27) + '\\[\\?\\d+l'
    code_reset_graphics_mode = chr(27) + '\\[00m'
    code_erase_display = chr(27) + '\\[2J'
    code_graphics_mode = chr(27) + '\\[\\d\\d;\\d\\dm'
    code_graphics_mode2 = chr(27) + '\\[\\d\\d;\\d\\d;\\d\\dm'
    code_get_cursor_position = chr(27) + '\\[6n'
    code_cursor_position = chr(27) + '\\[m'
    code_erase_display = chr(27) + '\\[J'
    code_attrs_off = chr(27) + '[0m'
    code_reverse = chr(27) + '[7m'
    code_set = [code_position_cursor, code_show_cursor, code_erase_line,
        code_enable_scroll, code_erase_start_line, code_form_feed,
        code_carriage_return, code_disable_line_wrapping,
        code_erase_line_end, code_reset_mode_screen_options,
        code_reset_graphics_mode, code_erase_display, code_graphics_mode,
        code_graphics_mode2, code_get_cursor_position, code_cursor_position,
        code_erase_display, code_attrs_off, code_reverse]
    output = string_buffer
    for ansi_esc_code in code_set:
        output = re.sub(ansi_esc_code, '', output)
    output = re.sub(code_next_line, self.RETURN, output)
    log.debug('new_output = {0}'.format(output))
    log.debug('repr = {0}'.format(repr(output)))
    return output