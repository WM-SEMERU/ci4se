def _clean_page_unique_slug_required(self, slug):
    if hasattr(self, 'instance') and self.instance.id:
        if Content.objects.exclude(page=self.instance).filter(body=slug,
            type='slug').count():
            raise forms.ValidationError(self.err_dict['another_page_error'])
    elif Content.objects.filter(body=slug, type='slug').count():
        raise forms.ValidationError(self.err_dict['another_page_error'])
    return slug