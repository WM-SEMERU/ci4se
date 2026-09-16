def accumulate(a_generator, cooperator=None):
    if cooperator:
        own_cooperate = cooperator.cooperate
    else:
        own_cooperate = cooperate
    spigot = ValueBucket()
    items = stream_tap((spigot,), a_generator)
    d = own_cooperate(items).whenDone()
    d.addCallback(accumulation_handler, spigot)
    return d