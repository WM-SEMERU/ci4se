def is_solid(regex):
    shape = re.sub('(\\\\.|[^\\[\\]\\(\\)\\|\\?\\+\\*])', '#', regex)
    skeleton = shape.replace('#', '')
    if len(shape) <= 1:
        return True
    if re.match('^\\[[^\\]]*\\][\\*\\+\\?]?$', shape):
        return True
    if re.match('^\\([^\\(]*\\)[\\*\\+\\?]?$', shape):
        return True
    if re.match('^\\(\\)#*?\\)\\)', skeleton):
        return True
    else:
        return False