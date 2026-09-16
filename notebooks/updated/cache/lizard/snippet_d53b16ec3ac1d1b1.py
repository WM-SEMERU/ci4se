def make_published(self, request, queryset):
    rows_updated = queryset.update(is_published=True)
    self.message_user(request, ungettext('%(count)d newsitem was published',
        '%(count)d newsitems were published', rows_updated) % {'count':
        rows_updated})