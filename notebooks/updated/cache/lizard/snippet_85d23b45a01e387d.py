def options(description, **kwargs):

    def set_notes(function):
        function.refactor_notes = {'name': function.__name__, 'category':
            'Miscellaneous', 'description': description, 'doc': getattr(
            function, '__doc__', ''), 'args': []}
        function.refactor_notes.update(kwargs)
        return function
    return set_notes