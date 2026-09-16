def is_uid(str):
    import re
    if len(str) != 16:
        return False
    pattern = '[^\\.a-f0-9]'
    if re.search(pattern, str.lower()):
        return False
    return True