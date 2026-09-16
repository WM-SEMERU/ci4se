def setup_lilypond_windows(path='default'):
    default = 'C:/Program Files (x86)/LilyPond/usr/bin'
    path_variable = os.environ['PATH'].split(';')
    if path == 'default':
        path_variable.append(default)
    else:
        path_variable.append(path)
    os.environ['PATH'] = ';'.join(path_variable)