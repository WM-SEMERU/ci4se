def get_related_entry_admin_url(entry):
    namespaces = {Document: 'wagtaildocs:edit', Link: 'wagtaillinks:edit',
        Page: 'wagtailadmin_pages:edit'}
    for cls, url in namespaces.iteritems():
        if issubclass(entry.content_type.model_class(), cls):
            return urlresolvers.reverse(url, args=(entry.object_id,))
    return ''