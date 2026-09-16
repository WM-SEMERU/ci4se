def init_with_context(self, context):
    items = self._visible_models(context['request'])
    for model, perms in items:
        if not (perms['change'] or perms.get('view', False)):
            continue
        title = model._meta.verbose_name_plural
        url = self._get_admin_change_url(model, context)
        item = MenuItem(title=title, url=url)
        self.children.append(item)