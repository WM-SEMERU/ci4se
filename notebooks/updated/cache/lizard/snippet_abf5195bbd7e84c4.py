def get_base_indentation(code, include_start=False):
    new_line_indentation = re_new_line_indentation[include_start].finditer(code
        )
    new_line_indentation = tuple(m.groups(0)[0] for m in new_line_indentation)
    if new_line_indentation:
        return min(new_line_indentation, key=len)
    else:
        return ''