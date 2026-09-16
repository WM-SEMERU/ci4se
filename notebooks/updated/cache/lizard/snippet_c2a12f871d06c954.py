def git_hook(strict=False):
    diff_cmd = (
        'git diff-index --cached --name-only --diff-filter=ACMRTUXB HEAD')
    files_modified = get_lines(diff_cmd)
    errors = 0
    for filename in files_modified:
        if filename.endswith('.py'):
            staged_cmd = 'git show :%s' % filename
            staged_contents = get_output(staged_cmd)
            sort = SortImports(file_path=filename, file_contents=
                staged_contents.decode(), check=True)
            if sort.incorrectly_sorted:
                errors += 1
    return errors if strict else 0