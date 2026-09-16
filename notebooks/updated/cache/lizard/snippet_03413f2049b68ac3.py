def valid_variable_identifier(string):
    string = str(string)
    try:
        exec('%s = None' % string)
        if string in dir(builtins):
            raise SyntaxError()
    except SyntaxError:
        raise ValueError(
            'The given name string `%s` does not define a valid variable identifier.  Valid identifiers do not contain characters like `-` or empty spaces, do not start with numbers, cannot be mistaken with Python built-ins like `for`...)'
             % string)