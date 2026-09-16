def get_image_field_display(self, field_name, field):
    image = getattr(self.instance, field_name)
    if image:
        fltr, _ = Filter.objects.get_or_create(spec='max-400x400')
        rendition = image.get_rendition(fltr)
        return rendition.img_tag
    return self.model_admin.get_empty_value_display()