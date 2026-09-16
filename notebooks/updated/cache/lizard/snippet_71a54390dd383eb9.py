def ShutdownInstance(r, instance, dry_run=False, no_remember=False, timeout=120
    ):
    query = {'dry-run': dry_run, 'no-remember': no_remember}
    content = {'timeout': timeout}
    return r.request('put', '/2/instances/%s/shutdown' % instance, query=
        query, content=content)