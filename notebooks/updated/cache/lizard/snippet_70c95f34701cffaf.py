def set_or_create(self, request, article, form, language):
    base_fields = ['slug', 'title', 'description', 'meta_description',
        'page_title', 'menu_title', 'image']
    cleaned_data = form.cleaned_data
    try:
        obj = self.get(article=article, language=language)
    except self.model.DoesNotExist:
        data = {}
        for name in base_fields:
            if name in cleaned_data:
                data[name] = cleaned_data[name]
        data['article'] = article
        data['language'] = language
        return self.create(**data)
    for name in base_fields:
        if name in form.base_fields:
            value = cleaned_data.get(name, None)
            setattr(obj, name, value)
    obj.save()
    return obj