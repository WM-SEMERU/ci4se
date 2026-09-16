def close_comments(self, request, queryset):
    queryset.update(comment_enabled=False)
    self.message_user(request, _(
        'Comments are now closed for selected entries.'))