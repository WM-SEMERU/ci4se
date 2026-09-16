def definition(self, suffix='', local=False, ctype=None, optionals=True,
    customdim=None, modifiers=None):
    kind = '({})'.format(self.kind) if self.kind is not None else ''
    cleanmods = [m for m in self.modifiers if m != '' and m != ' ' and not
        (local and ('intent' in m or m == 'optional')) and not (not
        optionals and m == 'optional')]
    if modifiers is not None:
        cleanmods.extend(modifiers)
    if len(cleanmods) > 0:
        mods = ', ' + ', '.join(cleanmods) + ' '
    else:
        mods = ' '
    if customdim is not None:
        dimension = '({})'.format(customdim)
    else:
        dimension = '({})'.format(self.dimension
            ) if self.dimension is not None else ''
    if self.default is None:
        default = ''
    elif '>' in self.default:
        default = ' ={}'.format(self.default
            ) if self.default is not None else ''
    else:
        default = ' = {}'.format(self.default
            ) if self.default is not None else ''
    name = '{}{}'.format(self.name, suffix)
    stype = self.dtype if ctype is None else ctype
    return '{}{}{}:: {}{}{}'.format(stype, kind, mods, name, dimension, default
        )