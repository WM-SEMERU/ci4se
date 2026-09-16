def sanitizeString(name):
    newString = name
    replaceTable = [('^', '^5e'), ('"', '^22'), ('<', '^3c'), ('?', '^3f'),
        ('*', '^2a'), ('=', '^3d'), ('+', '^2b'), ('>', '^3e'), ('|', '^7c'
        ), (',', '^2c')]
    for r in replaceTable:
        newString = newString.replace(r[0], r[1])
    for x in range(0, 33):
        newString = newString.replace(chr(x), hex(x + sanitizerNum).replace
            ('0x', '^'))
    replaceTable2 = [('/', '='), (':', '+'), ('.', ',')]
    for r in replaceTable2:
        newString = newString.replace(r[0], r[1])
    return newString