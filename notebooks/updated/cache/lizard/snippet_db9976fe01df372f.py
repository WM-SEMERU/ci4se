def returner_argspec(module=''):
    returners_ = salt.loader.returners(__opts__, [])
    return salt.utils.args.argspec_report(returners_, module)