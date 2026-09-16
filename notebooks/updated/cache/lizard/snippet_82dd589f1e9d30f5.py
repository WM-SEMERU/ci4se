def queryset(self, request, queryset):
    if self.value():
        parent = Question.objects.get(slug=self.value())
        return Choice.objects.child_of(parent).order_by('-id')
    return queryset