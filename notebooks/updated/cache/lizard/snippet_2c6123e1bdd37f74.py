def get_api_items(api_doc_fd):
    current_module = 'pandas'
    previous_line = current_section = current_subsection = ''
    position = None
    for line in api_doc_fd:
        line = line.strip()
        if len(line) == len(previous_line):
            if set(line) == set('-'):
                current_section = previous_line
                continue
            if set(line) == set('~'):
                current_subsection = previous_line
                continue
        if line.startswith('.. currentmodule::'):
            current_module = line.replace('.. currentmodule::', '').strip()
            continue
        if line == '.. autosummary::':
            position = 'autosummary'
            continue
        if position == 'autosummary':
            if line == '':
                position = 'items'
                continue
        if position == 'items':
            if line == '':
                position = None
                continue
            item = line.strip()
            func = importlib.import_module(current_module)
            for part in item.split('.'):
                func = getattr(func, part)
            yield '.'.join([current_module, item]
                ), func, current_section, current_subsection
        previous_line = line