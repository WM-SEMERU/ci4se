def keyboard(table, day=None):
    cols, group = 'realkey AS key, COUNT(*) AS count', 'realkey'
    where = (('day', day),) if day else ()
    counts_display = counts = db.fetch(table, cols, where, group, 'count DESC')
    if 'combos' == table:
        counts_display = db.fetch(table, 'key, COUNT(*) AS count', where,
            'key', 'count DESC')
    events = db.fetch(table, where=where, order='stamp')
    for e in events:
        e['dt'] = datetime.datetime.fromtimestamp(e['stamp'])
    stats, collatedevents = stats_keyboard(events, table)
    days, input = db.fetch('counts', order='day', type=table), 'keyboard'
    return bottle.template('heatmap.tpl', locals(), conf=conf)