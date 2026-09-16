def get_version(string):
    flags = re.S
    pattern = ".*__version__ = '(.*?)'"
    match = re.match(pattern=pattern, string=string, flags=flags)
    if match:
        return match.group(1)
    raise RuntimeError('No version string could be matched')