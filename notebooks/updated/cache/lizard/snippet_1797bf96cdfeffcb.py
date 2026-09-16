def generate_thumb(self, image):
    image_file = image.file
    picture = Image.open(image_file).convert('RGB')
    picture.thumbnail((10, 10))
    picture.filter(ImageFilter.GaussianBlur(radius=4))
    absolute_path = self.build_thumb_path(image)
    self.save_thumb(picture, absolute_path)