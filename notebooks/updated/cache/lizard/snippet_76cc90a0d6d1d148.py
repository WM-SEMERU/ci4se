def migrator(state):
    for tweak in ('tweak1', 'tweak2', 'tweak3'):
        del state[0][tweak]
        for convo in state[1]:
            if tweak in convo:
                del convo[tweak]
    return state