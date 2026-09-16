def pq(ui, repo, *pats, **opts):
    opts['quick'] = True
    return pending(ui, repo, *pats, **opts)