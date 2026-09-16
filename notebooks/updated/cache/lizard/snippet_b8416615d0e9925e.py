def from_string(cls, serialized):
    warnings.warn(
        'SlashSeparatedCourseKey is deprecated! Please use locator.CourseLocator'
        , DeprecationWarning, stacklevel=2)
    return CourseLocator.from_string(serialized)