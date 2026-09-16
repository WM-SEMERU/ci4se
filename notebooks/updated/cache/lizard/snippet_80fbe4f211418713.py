def create(cls, changes, ref, excluded_categories=set()):
    ref = dict(ref)
    obj = obj_deref(ref)
    if isinstance(obj, Category):
        if any(c.id in excluded_categories for c in obj.chain_query):
            return
    else:
        event = obj if isinstance(obj, Event) else obj.event
        if event.category not in g.setdefault(
            'livesync_excluded_categories_checked', {}):
            g.livesync_excluded_categories_checked[event.category
                ] = excluded_categories & set(event.category_chain)
        if g.livesync_excluded_categories_checked[event.category]:
            return
    try:
        agents = g.livesync_agents
    except AttributeError:
        agents = g.livesync_agents = LiveSyncAgent.query.all()
    for change in changes:
        for agent in agents:
            entry = cls(agent=agent, change=change, **ref)
            db.session.add(entry)
    db.session.flush()