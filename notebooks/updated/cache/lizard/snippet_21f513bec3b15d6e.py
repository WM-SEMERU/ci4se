def gcp(main=False):
    if main:
        return project() if _current_project is None else _current_project
    else:
        return gcp(True
            ) if _current_subproject is None else _current_subproject