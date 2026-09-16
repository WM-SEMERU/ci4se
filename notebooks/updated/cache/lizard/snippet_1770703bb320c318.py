def _handle_pagerange(pagerange):
    try:
        pr = re.compile('pp\\.\\s([0-9]+)\\-([0-9]+)')
        start, end = re.findall(pr, pagerange)[0]
    except IndexError:
        start = end = 0
    return unicode(start), unicode(end)