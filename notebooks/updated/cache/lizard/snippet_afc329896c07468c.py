def admin_tools_render_dashboard(context, location='index', dashboard=None):
    if dashboard is None:
        dashboard = get_dashboard(context, location)
    dashboard.init_with_context(context)
    dashboard._prepare_children()
    try:
        preferences = DashboardPreferences.objects.get(user=context[
            'request'].user, dashboard_id=dashboard.get_id()).data
    except DashboardPreferences.DoesNotExist:
        preferences = '{}'
        try:
            DashboardPreferences(user=context['request'].user, dashboard_id
                =dashboard.get_id(), data=preferences).save()
        except IntegrityError:
            pass
    context.update({'template': dashboard.template, 'dashboard': dashboard,
        'dashboard_preferences': preferences, 'split_at': math.ceil(float(
        len(dashboard.children)) / float(dashboard.columns)),
        'has_disabled_modules': len([m for m in dashboard.children if not m
        .enabled]) > 0, 'admin_url': reverse('%s:index' %
        get_admin_site_name(context))})
    return context