def normalize_collaboration(collaboration):
    if not collaboration:
        return []
    collaboration = collaboration.strip()
    if collaboration.startswith('(') and collaboration.endswith(')'):
        collaboration = collaboration[1:-1]
    collaborations = _RE_AND.split(collaboration)
    collaborations = (_RE_COLLABORATION_LEADING.sub('', collab) for collab in
        collaborations)
    collaborations = (_RE_COLLABORATION_TRAILING.sub('', collab) for collab in
        collaborations)
    return [collab.strip() for collab in collaborations]