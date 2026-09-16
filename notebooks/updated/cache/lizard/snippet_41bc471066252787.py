def _from_deprecated_string(cls, serialized):
    match = cls.DEPRECATED_URL_RE.match(serialized)
    if match is None:
        raise InvalidKeyError(BlockUsageLocator, serialized)
    groups = match.groupdict()
    course_key = CourseLocator(org=groups['org'], course=groups['course'],
        run=None, branch=groups.get('revision'), deprecated=True)
    return cls(course_key, groups['category'], groups['name'], deprecated=True)