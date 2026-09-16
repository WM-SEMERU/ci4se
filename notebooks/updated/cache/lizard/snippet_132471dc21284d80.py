def scourCoordinates(data, options, force_whitespace=False, control_points=
    [], flags=[]):
    if data is not None:
        newData = []
        c = 0
        previousCoord = ''
        for coord in data:
            is_control_point = c in control_points
            scouredCoord = scourUnitlessLength(coord, renderer_workaround=
                options.renderer_workaround, is_control_point=is_control_point)
            if c > 0 and (force_whitespace or scouredCoord[0].isdigit() or 
                scouredCoord[0] == '.' and not ('.' in previousCoord or 'e' in
                previousCoord)) and (c - 1 not in flags or options.
                renderer_workaround):
                newData.append(' ')
            newData.append(scouredCoord)
            previousCoord = scouredCoord
            c += 1
        if options.renderer_workaround:
            if len(newData) > 0:
                for i in range(1, len(newData)):
                    if newData[i][0] == '-' and 'e' in newData[i - 1]:
                        newData[i - 1] += ' '
                return ''.join(newData)
        else:
            return ''.join(newData)
    return ''