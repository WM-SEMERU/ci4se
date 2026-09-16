def convert_image_to_rgb_mode(image, fill_color=(255, 255, 255)):
    if image.mode not in ('RGBA', 'LA'):
        return image
    background_image = Image.new(image.mode[:-1], image.size, fill_color)
    background_image.paste(image, image.split()[-1])
    return background_image