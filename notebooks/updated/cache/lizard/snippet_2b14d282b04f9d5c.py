def modified_files(root, tracked_only=False, commit=None):
    assert os.path.isabs(root), 'Root has to be absolute, got: %s' % root
    command = ['hg', 'status']
    if commit:
        command.append('--change=%s' % commit)
    status_lines = subprocess.check_output(command).decode('utf-8').split(os
        .linesep)
    modes = ['M', 'A']
    if not tracked_only:
        modes.append('\\?')
    modes_str = '|'.join(modes)
    modified_file_status = utils.filter_lines(status_lines, 
        '(?P<mode>%s) (?P<filename>.+)' % modes_str, groups=('filename',
        'mode'))
    return dict((os.path.join(root, filename), mode) for filename, mode in
        modified_file_status)