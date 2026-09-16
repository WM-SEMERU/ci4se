def lastmod(self, category):
    lastitems = EntryModel.objects.published().order_by('-modification_date'
        ).filter(categories=category).only('modification_date')
    return lastitems[0].modification_date