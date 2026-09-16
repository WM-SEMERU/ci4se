def molecules2symbols(molecules, add_hydrogen=True):
    symbols = sorted(list(set(ase.symbols.string2symbols(''.join(map(lambda
        _x: ''.join(ase.symbols.string2symbols(_x)), molecules))))), key=lambda
        _y: ase.data.atomic_numbers[_y])
    if add_hydrogen and 'H' not in symbols:
        symbols.insert(0, 'H')
    return symbols