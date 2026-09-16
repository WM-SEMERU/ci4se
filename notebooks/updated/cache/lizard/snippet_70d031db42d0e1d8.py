def supported_fixes():
    yield 'E101', docstring_summary(reindent.__doc__)
    instance = FixPEP8(filename=None, options=None, contents='')
    for attribute in dir(instance):
        code = re.match('fix_([ew][0-9][0-9][0-9])', attribute)
        if code:
            yield code.group(1).upper(), re.sub('\\s+', ' ',
                docstring_summary(getattr(instance, attribute).__doc__))
    for code, function in sorted(global_fixes()):
        yield code.upper() + (4 - len(code)) * ' ', re.sub('\\s+', ' ',
            docstring_summary(function.__doc__))
    for code in sorted(CODE_TO_2TO3):
        yield code.upper() + (4 - len(code)) * ' ', re.sub('\\s+', ' ',
            docstring_summary(fix_2to3.__doc__))