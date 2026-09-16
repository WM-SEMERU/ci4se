def DeleteInstance(r, instance, dry_run=False):
    return r.request('delete', '/2/instances/%s' % instance, query={
        'dry-run': dry_run})