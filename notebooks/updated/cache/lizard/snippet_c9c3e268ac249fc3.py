def cache_call_signatures(source, user_pos, stmt):
    index = user_pos[0] - 1
    lines = source.splitlines() or ['']
    if source and source[-1] == '\n':
        lines.append('')
    before_cursor = lines[index][:user_pos[1]]
    other_lines = lines[stmt.start_pos[0]:index]
    whole = '\n'.join(other_lines + [before_cursor])
    before_bracket = re.match('.*\\(', whole, re.DOTALL)
    module_path = stmt.get_parent_until().path
    return None if module_path is None else (module_path, before_bracket,
        stmt.start_pos)