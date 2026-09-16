def get_env_dict(root_section):
    env_lago = defaultdict(dict)
    decider = re.compile(
        '^{0}(?:_(?!_)|(?P<has>__))(?(has)(?P<section>.+?)__)(?P<name>.+)$'
        .format(root_section.upper()))
    for key, value in os.environ.iteritems():
        match = decider.match(key)
        if not match:
            continue
        if not match.group('name') or not value:
            warn('empty environment variable definition:{0}, ignoring.'.
                format(key))
        else:
            section = match.group('section') or root_section
            env_lago[section.lower()][match.group('name').lower()] = value
    return dict(env_lago)