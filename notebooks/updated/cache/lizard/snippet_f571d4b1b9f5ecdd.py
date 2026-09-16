def _get_activate_script(cmd, venv):
    if 'fish' in cmd:
        suffix = '.fish'
        command = 'source'
    elif 'csh' in cmd:
        suffix = '.csh'
        command = 'source'
    else:
        suffix = ''
        command = '.'
    venv_location = str(venv).replace(' ', '\\ ')
    return ' {2} {0}/bin/activate{1}'.format(venv_location, suffix, command)