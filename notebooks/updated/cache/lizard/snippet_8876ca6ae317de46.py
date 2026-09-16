def get_converted_image_name(image):
    png_extension = '.png'
    if image[0 - len(png_extension):] == png_extension:
        return image
    img_dir = os.path.split(image)[0]
    image = os.path.split(image)[-1]
    if len(image.split('.')) > 1:
        old_extension = '.' + image.split('.')[-1]
        converted_image = image[:0 - len(old_extension)] + png_extension
    else:
        converted_image = image + png_extension
    return os.path.join(img_dir, converted_image)