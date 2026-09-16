def get_urls(self):
    urls = super(FormAdmin, self).get_urls()
    extra_urls = [url('^(?P<form_id>\\d+)/entries/$', self.admin_site.
        admin_view(self.entries_view), name='form_entries'), url(
        '^file/(?P<field_entry_id>\\d+)/$', self.admin_site.admin_view(self
        .file_view), name='form_file')]
    return extra_urls + urls