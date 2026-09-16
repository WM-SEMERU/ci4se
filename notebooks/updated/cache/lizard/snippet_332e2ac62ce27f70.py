def DeleteInstanceTags(r, instance, tags, dry_run=False):
    query = {'tag': tags, 'dry-run': dry_run}
    return r.request('delete', '/2/instances/%s/tags' % instance, query=query)