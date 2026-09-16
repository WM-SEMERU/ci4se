def get_queryset(self):
    self.category = get_category_or_404(self.kwargs['path'])
    return self.category.entries_published()