def get_python_symbol_icons(oedata):
    class_icon = ima.icon('class')
    method_icon = ima.icon('method')
    function_icon = ima.icon('function')
    private_icon = ima.icon('private1')
    super_private_icon = ima.icon('private2')
    symbols = process_python_symbol_data(oedata)
    fold_levels = sorted(list(set([s[2] for s in symbols])))
    parents = [None] * len(symbols)
    icons = [None] * len(symbols)
    indexes = []
    parent = None
    for level in fold_levels:
        for index, item in enumerate(symbols):
            line, name, fold_level, token = item
            if index in indexes:
                continue
            if fold_level == level:
                indexes.append(index)
                parent = item
            else:
                parents[index] = parent
    for index, item in enumerate(symbols):
        parent = parents[index]
        if item[-1] == 'def':
            icons[index] = function_icon
        elif item[-1] == 'class':
            icons[index] = class_icon
        else:
            icons[index] = QIcon()
        if parent is not None:
            if parent[-1] == 'class':
                if item[-1] == 'def' and item[1].startswith('__'):
                    icons[index] = super_private_icon
                elif item[-1] == 'def' and item[1].startswith('_'):
                    icons[index] = private_icon
                else:
                    icons[index] = method_icon
    return icons