def get_colors(img):
    w, h = img.size
    return [color[:3] for count, color in img.convert('RGB').getcolors(w * h)]