def regex_parse_template(self, template, pattern):
    groups = []
    literals = []
    replacements = _compile_replacement_helper(pattern, template)
    count = 0
    for part in replacements:
        if isinstance(part, int):
            literals.append(None)
            groups.append((count, part))
        else:
            literals.append(part)
        count += 1
    return groups, literals