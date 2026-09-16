def find_template(self, name, context, peeking=False):
    from django.conf import settings
    import django.template.loaders.app_directories as app_directories
    try:
        get_app_template_dirs = app_directories.get_app_template_dirs
        app_template_dirs = get_app_template_dirs('templates')
    except AttributeError:
        app_template_dirs = app_directories.app_template_dirs
    try:
        find_template_loader = context.template.engine.find_template_loader
        template_dirs = context.template.engine.dirs
        template_loaders = context.template.engine.loaders
    except AttributeError:
        from django.template.loader import find_template_loader
        template_dirs = list(settings.TEMPLATE_DIRS)
        template_loaders = settings.TEMPLATE_LOADERS
    context_name = 'OVEREXTENDS_DIRS'
    if context_name not in context:
        context[context_name] = {}
    if name not in context[context_name]:
        all_dirs = template_dirs + list(app_template_dirs)
        context[context_name][name] = list(map(os.path.abspath, all_dirs))
    loaders = []
    for loader_name in template_loaders:
        loader = find_template_loader(loader_name)
        loaders.extend(getattr(loader, 'loaders', [loader]))
    for loader in loaders:
        dirs = context[context_name][name]
        if not dirs:
            break
        try:
            source, path = loader.load_template_source(name, dirs)
        except TemplateDoesNotExist:
            pass
        else:
            if not peeking:
                remove_path = os.path.abspath(path[:-len(name) - 1])
                context[context_name][name].remove(remove_path)
            return Template(source)
    raise TemplateDoesNotExist(name)