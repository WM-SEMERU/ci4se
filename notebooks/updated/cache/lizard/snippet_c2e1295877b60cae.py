def tag_list(self, other_model=None, queryset=None):
    from taggit.models import Tag
    return Tag.objects.filter(id__in=self._taglist(other_model, queryset))