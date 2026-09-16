def Instance(reactor=None):
    if NodeLeader._LEAD is None:
        NodeLeader._LEAD = NodeLeader(reactor)
    return NodeLeader._LEAD