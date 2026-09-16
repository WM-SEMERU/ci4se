def absl_to_standard(level):
    if not isinstance(level, int):
        raise TypeError('Expect an int level, found {}'.format(type(level)))
    if level < ABSL_FATAL:
        level = ABSL_FATAL
    if level <= ABSL_DEBUG:
        return ABSL_TO_STANDARD[level]
    return STANDARD_DEBUG - level + 1