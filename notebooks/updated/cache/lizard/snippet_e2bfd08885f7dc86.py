def reservoirLink(lines):
    KEYWORDS = ('LINK', 'RESERVOIR', 'RES_MINWSE', 'RES_INITWSE',
        'RES_MAXWSE', 'RES_NUMPTS', 'LAKE', 'MINWSE', 'INITWSE', 'MAXWSE',
        'NUMPTS')
    result = {'header': {'link': None, 'res_minwse': None, 'res_initwse':
        None, 'res_maxwse': None, 'res_numpts': None, 'minwse': None,
        'initwse': None, 'maxwse': None, 'numpts': None}, 'type': None,
        'points': []}
    pair = {'i': None, 'j': None}
    chunks = pt.chunk(KEYWORDS, lines)
    for key, chunkList in iteritems(chunks):
        for chunk in chunkList:
            schunk = chunk[0].strip().split()
            if key in ('NUMPTS', 'RES_NUMPTS'):
                result['header'][key.lower()] = schunk[1]
                for idx in range(1, len(chunk)):
                    schunk = chunk[idx].strip().split()
                    for count, ordinate in enumerate(schunk):
                        if count % 2 == 0:
                            pair['i'] = ordinate
                        else:
                            pair['j'] = ordinate
                            result['points'].append(pair)
                            pair = {'i': None, 'j': None}
            elif key in ('LAKE', 'RESERVOIR'):
                result['type'] = schunk[0]
            else:
                result['header'][key.lower()] = schunk[1]
    return result