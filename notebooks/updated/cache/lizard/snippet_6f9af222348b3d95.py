def is_muted(what):
    state = False
    for item in solo:
        if item not in what:
            state = True
        else:
            state = False
            break
    for item in mute:
        if item in what:
            state = True
            break
    return state