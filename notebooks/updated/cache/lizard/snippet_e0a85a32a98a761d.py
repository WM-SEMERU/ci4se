def changelist_view(self, request, extra_context=None):
    model = self.model
    if model.objects.all().count() > 1:
        return super(HTMLSitemapAdmin, self).changelist_view(request)
    else:
        obj = model.singleton.get()
        return redirect(reverse('admin:jmbo_sitemap_%s_change' % model.
            _meta.module_name, args=(obj.id,)))