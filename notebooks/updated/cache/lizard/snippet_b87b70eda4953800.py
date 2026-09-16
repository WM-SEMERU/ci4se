def box(text, width=100, height=3, corner='+', horizontal='-', vertical='|'):
    if width <= len(text) - 4:
        print('width is not large enough! apply auto-adjust...')
        width = len(text) + 4
    if height <= 2:
        print('height is too small! apply auto-adjust...')
        height = 3
    if height % 2 == 0:
        print('height has to be odd! apply auto-adjust...')
        height += 1
    head = tail = corner + horizontal * (width - 2) + corner
    pad = '%s%s%s' % (vertical, ' ' * (width - 2), vertical)
    pad_number = (height - 3) // 2
    pattern = '{: ^%s}' % (width - 2,)
    body = vertical + pattern.format(text) + vertical
    return '\n'.join([head] + [pad] * pad_number + [body] + [pad] *
        pad_number + [tail])