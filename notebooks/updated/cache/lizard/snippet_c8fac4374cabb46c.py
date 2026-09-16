def nl2br(s):
    if not isinstance(s, basestring):
        s = str(s)
    s = re.sub('\\r\\n|\\r|\\n', '\n', s)
    paragraphs = re.split('\n{2,}', s)
    paragraphs = [('<p>%s</p>' % p.strip().replace('\n', '<br />')) for p in
        paragraphs]
    return '\n\n'.join(paragraphs)