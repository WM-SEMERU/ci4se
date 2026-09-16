def parse_combo(self, combo, modes_set, modifiers_set, pfx):
    mode, mods, trigger = None, set([]), combo
    if '+' in combo:
        if combo.endswith('+'):
            trigger, combo = '+', combo[:-1]
            if '+' in combo:
                items = set(combo.split('+'))
            else:
                items = set(combo)
        else:
            items = combo.split('+')
            trigger, items = items[-1], set(items[:-1])
        if '*' in items:
            items.remove('*')
            mods = '*'
        else:
            mods = items.intersection(modifiers_set)
        mode = items.intersection(modes_set)
        if len(mode) == 0:
            mode = None
        else:
            mode = mode.pop()
    if pfx is not None:
        trigger = pfx + trigger
    return mode, mods, trigger