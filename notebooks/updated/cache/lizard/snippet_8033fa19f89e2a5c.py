def get_urlpatterns(self):
    return [path('', search_view_factory(view_class=self.search_view,
        form_class=self.search_form), name='search')]