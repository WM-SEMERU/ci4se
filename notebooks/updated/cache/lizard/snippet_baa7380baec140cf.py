def filenamify(title):
    title = ensure_unicode(title)
    title = unicodedata.normalize('NFD', title)
    title = re.sub('[^a-z0-9 .-]', '', title.lower().strip())
    title = re.sub('\\s+', '.', title)
    title = re.sub('\\.-\\.', '-', title)
    return title