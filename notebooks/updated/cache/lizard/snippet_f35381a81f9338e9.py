def themeble(name, themes=None, global_context=None):

    def wrap(obj):
        context = global_context or inspect.stack()[1][0].f_globals
        if name in context and not getattr(context[name], '__themeble', False):
            raise RuntimeError('Name {} already exists in this context!'.
                format(name))
        if (themes and settings.CURRENT_THEME in themes or themes is None and
            name not in context):
            context[name] = obj
            obj.__themeble = True
        return obj
    return wrap