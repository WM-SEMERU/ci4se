def keep_entry_value(entry, values, converter, regex):
    return not any(converter(num) in values for num in regex.findall(entry))