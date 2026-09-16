def is_changed():
    executed, changed_lines = execute_git('status --porcelain', output=False)
    merge_not_finished = mod_path.exists('.git/MERGE_HEAD')
    return changed_lines.strip() or merge_not_finished