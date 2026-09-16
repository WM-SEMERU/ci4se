def add(class_, name, value, sep=';'):
    values = class_.get_values_list(name, sep)
    if value in values:
        return
    new_value = sep.join(values + [value])
    winreg.SetValueEx(class_.key, name, 0, winreg.REG_EXPAND_SZ, new_value)
    class_.notify()