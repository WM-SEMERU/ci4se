def keep_only_update_source_in_field(field, root, head, update):
    update_sources = {source.lower() for source in get_value(thaw(update),
        '.'.join([field, 'source']), [])}
    if len(update_sources) != 1:
        return root, head, update
    source = update_sources.pop()
    if field in root:
        root = root.set(field, remove_elements_with_source(source, root[field])
            )
    if field in head:
        head = head.set(field, remove_elements_with_source(source, head[field])
            )
    return root, head, update