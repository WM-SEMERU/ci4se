def draw_pin(text, background_color='green', font_color='white'):
    image = Image.new('RGB', (120, 20))
    draw = ImageDraw.Draw(image)
    draw.rectangle([(1, 1), (118, 18)], fill=color(background_color))
    draw.text((10, 4), text, fill=color(font_color))
    return image