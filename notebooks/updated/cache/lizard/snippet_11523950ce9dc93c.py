def _parse_name(self, field, boxscore):
    scheme = BOXSCORE_SCHEME[field]
    name = boxscore(scheme)
    if 'cbb/schools' not in str(name):
        name = re.sub('.*name">', '', str(name))
        name = re.sub('<.*', '', str(name))
    return name