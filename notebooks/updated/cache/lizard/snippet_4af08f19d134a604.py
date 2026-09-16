def split_docstring(docstring):
    docstring_list = [line.strip() for line in docstring.splitlines()]
    description_list = list(takewhile(lambda line: not (line.startswith(':'
        ) or line.startswith('@inherit')), docstring_list))
    description = ' '.join(description_list).strip()
    first_field_line_number = len(description_list)
    fields = []
    if first_field_line_number >= len(docstring_list):
        return description, fields
    last_field_lines = [docstring_list[first_field_line_number]]
    for line in docstring_list[first_field_line_number + 1:]:
        if line.strip().startswith(':') or line.strip().startswith('@inherit'):
            fields.append(' '.join(last_field_lines))
            last_field_lines = [line]
        else:
            last_field_lines.append(line)
    fields.append(' '.join(last_field_lines))
    return description, fields