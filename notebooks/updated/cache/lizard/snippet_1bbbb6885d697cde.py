def contains_entity(entity, text):
    try:
        entity = re.escape(entity)
        entity = entity.replace('\\ ', '([^\\w])?')
        pattern = '(\\ |-|\\\\|/|\\.|,|^)%s(\\ |\\-|\\\\|/|\\.|,|$)' % entity
        found = len(re.findall(pattern, text, re.I | re.M))
    except Exception as e:
        found = False
    return found