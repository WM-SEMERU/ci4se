def get_conf(cls, builder, doctree=None):
    result = {'theme': builder.config.slide_theme, 'autoslides': builder.
        config.autoslides, 'slide_classes': []}
    if doctree:
        conf_node = cls.get(doctree)
        if conf_node:
            result.update(conf_node.attributes)
    return result