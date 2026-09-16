def init_with_context(self, context):
    listitems = self._visible_models(context['request'])
    models = [{'name': model._meta.model_name, 'app_name': model._meta.
        app_label, 'title': capfirst(model._meta.verbose_name_plural),
        'url': self._get_admin_change_url(model, context)} for model, perms in
        listitems if self.is_item_visible(model, perms)]
    sort_cms_models(models)
    for model in models:
        self.children.append(items.MenuItem(title=model['title'], url=model
            ['url']))