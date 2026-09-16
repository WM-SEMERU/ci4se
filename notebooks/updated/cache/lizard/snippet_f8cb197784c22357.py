def post(self, request, pk=None):
    self.top_level_forum = get_object_or_404(Forum, pk=pk) if pk else None
    return self.mark_as_read(request, pk)