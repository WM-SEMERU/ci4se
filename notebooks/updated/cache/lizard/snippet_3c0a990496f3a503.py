def _rel_import(module, tgt):
    try:
        exec('from .' + module + ' import ' + tgt, globals(), locals())
    except SyntaxError:
        exec('from ' + module + ' import ' + tgt, globals(), locals())
    except (ValueError, SystemError):
        exec('from ' + module + ' import ' + tgt, globals(), locals())
    return eval(tgt)