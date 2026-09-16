def pages(site_id):
    start = int(flask.request.args.get('start', 0))
    end = int(flask.request.args.get('end', start + 90))
    reql = rr.table('pages').between([site_id, 1, r.minval], [site_id, r.
        maxval, r.maxval], index='least_hops').order_by(index='least_hops')[
        start:end]
    logging.debug('querying rethinkdb: %s', reql)
    pages_ = reql.run()
    return flask.jsonify(pages=list(pages_))