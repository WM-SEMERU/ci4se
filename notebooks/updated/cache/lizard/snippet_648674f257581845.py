def event_doctree_resolved(app, doctree, _):
    album_cache = app.builder.env.imgur_album_cache
    image_cache = app.builder.env.imgur_image_cache
    for node in doctree.traverse(ImgurTextNode):
        cache = album_cache if node.album else image_cache
        if node.name == 'imgur-description':
            text = cache[node.imgur_id].description
        else:
            text = cache[node.imgur_id].title
        node.replace_self([docutils.nodes.Text(text)])
    for node in doctree.traverse(ImgurImageNode):
        if node.album and not album_cache[node.imgur_id].cover_id:
            app.warn(
                'Album cover Imgur ID for {} not available in local cache.'
                .format(node.imgur_id))
            node.replace_self([docutils.nodes.Text('')])
        else:
            node.finalize(album_cache, image_cache, lambda m: app.builder.
                env.warn_node(m, node))