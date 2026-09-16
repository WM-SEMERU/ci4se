def plural(formatter, value, name, option, format):
    words = format.split('|')
    if not name and len(words) == 1:
        return
    try:
        number = decimal.Decimal(value)
    except (ValueError, decimal.InvalidOperation):
        return
    locale = Locale.parse(option) if option else formatter.locale
    index = get_plural_tag_index(number, locale)
    return formatter.format(words[index], value)