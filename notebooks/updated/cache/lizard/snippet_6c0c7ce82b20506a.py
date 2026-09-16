def save_load(jid, load, minions=None):
    signaled = dispatch.Signal(providing_args=['jid', 'load']).send(sender=
        'save_load', jid=jid, load=load)
    for signal in signaled:
        log.debug(
            "Django returner function 'save_load' signaled %s which responded with %s"
            , signal[0], signal[1])