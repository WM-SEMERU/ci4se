def allow(self, comment, content_object, request):
    if self.enable_field:
        if not getattr(content_object, self.enable_field):
            return False
    if self.auto_close_field and self.close_after is not None:
        close_after_date = getattr(content_object, self.auto_close_field)
        if close_after_date is not None and self._get_delta(timezone.now(),
            close_after_date).days >= self.close_after:
            return False
    return True