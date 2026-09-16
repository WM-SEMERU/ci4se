def _parse_local_version(local):
    if local is not None:
        return tuple(part.lower() if not part.isdigit() else int(part) for
            part in _local_version_separators.split(local))