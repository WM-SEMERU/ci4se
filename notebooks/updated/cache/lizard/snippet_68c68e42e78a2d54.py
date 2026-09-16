def admin_dropdown_menu(context):
    template_vars = context.flatten()
    user = context['request'].user
    if user.is_staff:
        template_vars['dropdown_menu_app_list'] = admin_app_list(context[
            'request'])
        if user.is_superuser:
            sites = Site.objects.all()
        else:
            try:
                sites = user.sitepermissions.sites.all()
            except ObjectDoesNotExist:
                sites = Site.objects.none()
        template_vars['dropdown_menu_sites'] = list(sites)
        template_vars['dropdown_menu_selected_site_id'] = current_site_id()
        template_vars['settings'] = context['settings']
        template_vars['request'] = context['request']
        return template_vars