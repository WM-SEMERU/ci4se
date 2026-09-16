def xSectionChunk(lines):
    KEYWORDS = ('MANNINGS_N', 'BOTTOM_WIDTH', 'BANKFULL_DEPTH',
        'SIDE_SLOPE', 'NPAIRS', 'NUM_INTERP', 'X1', 'ERODE', 'MAX_EROSION',
        'SUBSURFACE', 'M_RIVER', 'K_RIVER')
    result = {'mannings_n': None, 'bottom_width': None, 'bankfull_depth':
        None, 'side_slope': None, 'npairs': None, 'num_interp': None,
        'erode': False, 'subsurface': False, 'max_erosion': None, 'm_river':
        None, 'k_river': None, 'breakpoints': []}
    chunks = pt.chunk(KEYWORDS, lines)
    for key, chunkList in iteritems(chunks):
        for chunk in chunkList:
            schunk = chunk[0].strip().split()
            if key == 'X1':
                x = schunk[1]
                y = schunk[2]
                result['breakpoints'].append({'x': x, 'y': y})
            if key in ('SUBSURFACE', 'ERODE'):
                result[key.lower()] = True
            else:
                result[key.lower()] = schunk[1]
    return result