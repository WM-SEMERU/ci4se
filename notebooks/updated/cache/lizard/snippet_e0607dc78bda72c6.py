def restore_logging(lines, min_level_value, max_level_value):
    output = ''
    while lines:
        line = lines[0]
        if line.lstrip() != PASS_LINE_CONTENTS:
            output += line
            lines = lines[1:]
        else:
            logging_lines, remaining_lines = split_call(lines[1:])
            lines = remaining_lines
            logging_stmt = ''.join(logging_lines)
            original_lines = line + logging_stmt
            if not check_level(logging_stmt, True, min_level_value,
                max_level_value):
                output += logging_stmt
            else:
                uncommented_logging_lines = uncomment_lines(logging_lines)
                logging.info('replacing:\n%s\nwith this:\n%s' % (
                    original_lines.rstrip(), uncommented_logging_lines.
                    rstrip()))
                output += uncommented_logging_lines
    return output