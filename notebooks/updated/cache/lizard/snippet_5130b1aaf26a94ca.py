def pep8_lines_between_cells(prev_lines, next_lines, ext):
    if not next_lines:
        return 1
    if not prev_lines:
        return 0
    if ext != '.py':
        return 1
    if cell_ends_with_function_or_class(prev_lines):
        return 2 if cell_has_code(next_lines) else 1
    if cell_ends_with_code(prev_lines
        ) and next_instruction_is_function_or_class(next_lines):
        return 2
    return 1