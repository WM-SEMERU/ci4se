def generate_completions(frame, act_tok):
    if frame is None:
        return []
    updated_globals = {}
    updated_globals.update(frame.f_globals)
    updated_globals.update(frame.f_locals)
    if pydevconsole.IPYTHON:
        completions = pydevconsole.get_completions(act_tok, act_tok,
            updated_globals, frame.f_locals)
    else:
        completer = Completer(updated_globals, None)
        completions = completer.complete(act_tok)
    return completions