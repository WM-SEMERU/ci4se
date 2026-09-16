def get_app_index_dashboard(context):
    app = context['app_list'][0]
    model_list = []
    app_label = None
    app_title = app['name']
    admin_site = get_admin_site(context=context)
    for model, model_admin in admin_site._registry.items():
        if app['app_label'] == model._meta.app_label:
            split = model.__module__.find(model._meta.app_label)
            app_label = model.__module__[0:split] + model._meta.app_label
            for m in app['models']:
                if m['name'] == capfirst(model._meta.verbose_name_plural):
                    mod = '%s.%s' % (model.__module__, model.__name__)
                    model_list.append(mod)
    if app_label is not None and app_label in Registry.registry:
        return Registry.registry[app_label](app_title, model_list)
    return _get_dashboard_cls(getattr(settings,
        'ADMIN_TOOLS_APP_INDEX_DASHBOARD',
        'admin_tools.dashboard.dashboards.DefaultAppIndexDashboard'), context)(
        app_title, model_list)