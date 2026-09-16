def adjust_name_for_printing(name):
    if name is not None:
        name2 = name
        name = name.replace(' ', '_').replace('.', '_').replace('-', '_m_')
        name = name.replace('+', '_p_').replace('!', '_I_')
        name = name.replace('**', '_xx_').replace('*', '_x_')
        name = name.replace('/', '_l_').replace('@', '_at_')
        name = name.replace('(', '_of_').replace(')', '')
        if re.match('^[a-zA-Z_][a-zA-Z0-9-_]*$', name) is None:
            raise NameError(
                'name {} converted to {} cannot be further converted to valid python variable name!'
                .format(name2, name))
        return name
    return ''