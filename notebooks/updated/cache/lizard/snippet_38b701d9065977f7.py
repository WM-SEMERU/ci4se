def get_text_alignment(pos):
    pos = pos.lower()
    va, ha = None, None
    if pos == 'nw':
        va, ha = 'top', 'left'
    elif pos == 'ne':
        va, ha = 'top', 'right'
    elif pos == 'sw':
        va, ha = 'bottom', 'left'
    elif pos == 'se':
        va, ha = 'bottom', 'right'
    else:
        raise ValueError("Unknown value for 'pos': %s" % str(pos))
    return {'va': va, 'ha': ha}