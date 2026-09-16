def get_sub_menu_template_names(self):
    template_names = []
    menu_name = self.menu_short_name
    site = self._contextual_vals.current_site
    level = self._contextual_vals.current_level
    if settings.SITE_SPECIFIC_TEMPLATE_DIRS and site:
        hostname = site.hostname
        template_names.extend(['menus/%s/%s/level_%s.html' % (hostname,
            menu_name, level), 'menus/%s/%s/sub_menu.html' % (hostname,
            menu_name), 'menus/%s/%s_sub_menu.html' % (hostname, menu_name),
            'menus/%s/sub_menu.html' % hostname])
    template_names.extend(['menus/%s/level_%s.html' % (menu_name, level), 
        'menus/%s/sub_menu.html' % menu_name, 'menus/%s_sub_menu.html' %
        menu_name, settings.DEFAULT_SUB_MENU_TEMPLATE])
    return template_names