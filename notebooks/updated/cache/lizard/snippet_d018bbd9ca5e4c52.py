def check_path(filename, reporter=modReporter.Default, settings_path=None,
    **setting_overrides):
    try:
        with open(filename, 'U') as f:
            codestr = f.read() + '\n'
    except UnicodeError:
        reporter.unexpected_error(filename, 'problem decoding source')
        return 1
    except IOError:
        msg = sys.exc_info()[1]
        reporter.unexpected_error(filename, msg.args[1])
        return 1
    return check(codestr, filename, reporter, settings_path, **
        setting_overrides)