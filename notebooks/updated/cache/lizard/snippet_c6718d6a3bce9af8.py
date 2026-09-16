def register_archive_format(name, function, extra_args=None, description=''):
    if extra_args is None:
        extra_args = []
    if not isinstance(function, collections.Callable):
        raise TypeError('The %s object is not callable' % function)
    if not isinstance(extra_args, (tuple, list)):
        raise TypeError('extra_args needs to be a sequence')
    for element in extra_args:
        if not isinstance(element, (tuple, list)) or len(element) != 2:
            raise TypeError('extra_args elements are : (arg_name, value)')
    _ARCHIVE_FORMATS[name] = function, extra_args, description