def discover():
    candidate_path = os.path.abspath(os.path.join(os.curdir, os.pardir, 'data')
        )
    if os.path.exists(candidate_path):
        return Project(os.path.abspath(os.path.join(candidate_path, os.pardir))
            )
    candidate_path = os.path.abspath(os.path.join(os.curdir, 'data'))
    if os.path.exists(candidate_path):
        return Project(os.path.abspath(os.curdir))
    candidate_path = os.path.abspath(os.path.join(os.curdir, os.pardir, 'data')
        )
    if os.path.exists(candidate_path):
        return Project(os.path.abspath(os.path.join(candidate_path, os.
            pardir, os.pardir)))
    raise ValueError(
        'Cannot discover the structure of the project. Make sure that the data directory exists'
        )