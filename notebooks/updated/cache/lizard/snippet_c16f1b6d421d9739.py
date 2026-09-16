def _simplify(elements):
    simplified = []
    previous = None
    for element in elements:
        if element == '..':
            raise FormicError("Invalid glob: Cannot have '..' in a glob: {0}"
                .format('/'.join(elements)))
        elif element == '.':
            pass
        elif element == '**' and previous == '**':
            pass
        else:
            simplified.append(os.path.normcase(element))
            previous = element
    if simplified[-1] == '':
        simplified[-1] = '**'
    if simplified[0] == '':
        del simplified[0]
    elif simplified[0] != '**':
        simplified.insert(0, '**')
    return simplified