def get_ls_l_desc(desc, include_folder=False, include_project=False):
    if 'state' in desc:
        state_len = len(desc['state'])
        if desc['state'] != 'closed':
            state_str = YELLOW() + desc['state'] + ENDC()
        else:
            state_str = GREEN() + desc['state'] + ENDC()
    else:
        state_str = ''
        state_len = 0
    name_str = ''
    if include_folder:
        name_str += desc['folder'] + ('/' if desc['folder'] != '/' else '')
    name_str += desc['name']
    if desc['class'] in ['applet', 'workflow']:
        name_str = BOLD() + GREEN() + name_str + ENDC()
    size_str = ''
    if 'size' in desc and desc['class'] == 'file':
        size_str = get_size_str(desc['size'])
    elif 'length' in desc:
        size_str = str(desc['length']) + ' rows'
    size_padding = ' ' * max(0, 9 - len(size_str))
    return state_str + DELIMITER(' ' * (8 - state_len)
        ) + render_short_timestamp(desc['modified']) + DELIMITER(' '
        ) + size_str + DELIMITER(size_padding + ' ') + name_str + DELIMITER(
        ' (') + (desc['project'] + DELIMITER(':') if include_project else ''
        ) + desc['id'] + DELIMITER(')')