def sanitize_version(version):
    if hasattr(version, 'base_version'):
        if version.base_version:
            parts = version.base_version.split('.')
        else:
            parts = []
    else:
        parts = []
        for part in version:
            if part.startswith('*'):
                break
            parts.append(part)
    parts = [int(p) for p in parts]
    if len(parts) < 3:
        parts += [0] * (3 - len(parts))
    major, minor, micro = parts[:3]
    cleaned_version = '{}.{}.{}'.format(major, minor, micro)
    return cleaned_version