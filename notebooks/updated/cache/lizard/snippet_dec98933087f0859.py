def inurl(needles, haystack, position='any'):
    count = 0
    haystack2 = haystack.lower()
    for needle in needles:
        needle2 = needle.lower()
        if position == 'any':
            if haystack2.find(needle2) > -1:
                count += 1
        elif position == 'end':
            if haystack2.endswith(needle2):
                count += 1
        elif position == 'begin':
            if haystack2.startswith(needle2):
                count += 1
    if count > 0:
        return True
    return False