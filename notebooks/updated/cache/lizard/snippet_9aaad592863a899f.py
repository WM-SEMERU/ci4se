def unmark_featured(self, request, queryset):
    queryset.update(featured=False)
    self.message_user(request, _(
        'Selected entries are no longer marked as featured.'))