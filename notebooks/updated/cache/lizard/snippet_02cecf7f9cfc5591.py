def _diff_group(group):
    yield _diff_group_position(group)
    for old_line, new_line, line_or_conflict in group:
        if isinstance(line_or_conflict, tuple):
            old, new = line_or_conflict
            for o in old:
                yield color.Deleted('-' + o.strip('\n'))
            if new and old and new[-1].endswith('\n') and not old[-1].endswith(
                '\n'):
                yield '\\ No newline at end of file'
            for n in new:
                yield color.Added('+' + n.strip('\n'))
            if old and new and old[-1].endswith('\n') and not new[-1].endswith(
                '\n'):
                yield '\\ No newline at end of file'
        else:
            yield ' ' + line_or_conflict.strip('\n')