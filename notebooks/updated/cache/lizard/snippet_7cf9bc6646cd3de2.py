def process_marked_lines(lines, markers, return_flags=[False, -1, -1]):
    markers = ''.join(markers)
    if 's' not in markers and not re.search('(me*){3}', markers):
        markers = markers.replace('m', 't')
    if re.match('[te]*f', markers):
        return_flags[:] = [False, -1, -1]
        return lines
    for inline_reply in re.finditer('(?<=m)e*(t[te]*)m', markers):
        links = RE_PARENTHESIS_LINK.search(lines[inline_reply.start() - 1]
            ) or RE_PARENTHESIS_LINK.match(lines[inline_reply.start()].strip())
        if not links:
            return_flags[:] = [False, -1, -1]
            return lines
    quotation = re.search('(se*)+((t|f)+e*)+', markers)
    if quotation:
        return_flags[:] = [True, quotation.start(), len(lines)]
        return lines[:quotation.start()]
    quotation = RE_QUOTATION.search(markers) or RE_EMPTY_QUOTATION.search(
        markers)
    if quotation:
        return_flags[:] = True, quotation.start(1), quotation.end(1)
        return lines[:quotation.start(1)] + lines[quotation.end(1):]
    return_flags[:] = [False, -1, -1]
    return lines