def get_canonical_url(metadata, request):
    slug_title = '/{}'.format('-'.join(metadata['title'].split()))
    settings = get_current_registry().settings
    canon_host = settings.get('canonical-hostname', re.sub('archive.', '',
        request.host))
    if metadata['canonical'] is None:
        canon_url = request.route_url('content', ident_hash=metadata['id'],
            ignore=slug_title)
    else:
        canon_url = request.route_url('content', ident_hash=metadata[
            'canonical'], separator=':', page_ident_hash=metadata['id'],
            ignore=slug_title)
    return re.sub(request.host, canon_host, canon_url)