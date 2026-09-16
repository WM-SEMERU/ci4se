def get_cloud_front_origin_access_identities_by_comment(Comment, region=
    None, key=None, keyid=None, profile=None):
    log.debug(
        'Dereferincing CloudFront origin access identity `%s` by Comment.',
        Comment)
    ret = list_cloud_front_origin_access_identities(region=region, key=key,
        keyid=keyid, profile=profile)
    if ret is None:
        return ret
    items = []
    for item in ret:
        comment = item.get('Comment', '')
        if comment == Comment or comment.startswith('{0}:'.format(Comment)):
            items += [item]
    return items