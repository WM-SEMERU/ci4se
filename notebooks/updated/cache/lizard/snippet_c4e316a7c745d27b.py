def pil_image_to_django_file(self, pil_image):
    if pil_image.mode not in ('L', 'RGB'):
        pil_image = pil_image.convert('RGB')
    temp_io = six.BytesIO()
    pil_image.save(temp_io, 'JPEG', quality=self.IMAGE_QUALITY, optimize=
        True, progressive=True, icc_profile=pil_image.info.get('icc_profile'))
    temp_io.seek(0)
    django_file = ContentFile(temp_io.getvalue())
    return django_file