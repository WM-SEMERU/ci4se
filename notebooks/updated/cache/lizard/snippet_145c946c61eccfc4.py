def get_parent_info(brain_or_object, endpoint=None):
    if is_root(brain_or_object):
        return {}
    parent = get_parent(brain_or_object)
    portal_type = get_portal_type(parent)
    resource = portal_type_to_resource(portal_type)
    if endpoint is None:
        endpoint = get_endpoint(parent)
    return {'parent_id': get_id(parent), 'parent_uid': get_uid(parent),
        'parent_url': url_for(endpoint, resource=resource, uid=get_uid(parent))
        }