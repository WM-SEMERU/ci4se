def render(request, templates, dictionary=None, context_instance=None, **kwargs
    ):
    warnings.warn(
        "yacms.utils.views.render is deprecated and will be removed in a future version. Please update your project to use Django's TemplateResponse, which now provides equivalent functionality."
        , DeprecationWarning)
    dictionary = dictionary or {}
    if context_instance:
        context_instance.update(dictionary)
    else:
        context_instance = RequestContext(request, dictionary)
    return TemplateResponse(request, templates, context_instance, **kwargs)