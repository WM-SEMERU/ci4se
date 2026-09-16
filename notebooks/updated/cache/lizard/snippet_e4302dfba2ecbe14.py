def as_urlpatterns(self):
    urls = []
    for action in self.actions:
        view_class = self.view_for_action(action)
        view_pattern = self.pattern_for_view(view_class, action)
        name = self.url_name_for_action(action)
        urls.append(url(view_pattern, view_class.as_view(), name=name))
    return urls