def _cleanupConnections(senderkey, signal):
    try:
        receivers = connections[senderkey][signal]
    except:
        pass
    else:
        if not receivers:
            try:
                signals = connections[senderkey]
            except KeyError:
                pass
            else:
                del signals[signal]
                if not signals:
                    _removeSender(senderkey)