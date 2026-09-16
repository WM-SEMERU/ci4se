def import_symbol(name=None, path=None, typename=None, base_path=None):
    _, symbol = _import(name or typename, path or base_path)
    return symbol