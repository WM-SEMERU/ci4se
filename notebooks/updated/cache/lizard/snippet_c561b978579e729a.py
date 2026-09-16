def django_file_to_pil_image(self, django_file):
    django_file.open()
    pil_image = Image.open(django_file.file)
    return pil_image