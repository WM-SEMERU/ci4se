def lastmod(self, tag):
    lastitems = EntryModel.objects.published().order_by('-modification_date'
        ).filter(tags=tag).only('modification_date')
    return lastitems[0].modification_date