def normalize_locale(locale):
    import re
    match = re.match('^[a-z]+', locale.lower())
    if match:
        return match.group()