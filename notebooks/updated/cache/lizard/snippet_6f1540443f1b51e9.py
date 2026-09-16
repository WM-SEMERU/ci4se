def round_rectangle(size, radius, fill):
    width, height = size
    rectangle = Image.new('L', size, 255)
    corner = round_corner(radius, 255)
    rectangle.paste(corner, (0, 0))
    rectangle.paste(corner.rotate(90), (0, height - radius))
    rectangle.paste(corner.rotate(180), (width - radius, height - radius))
    rectangle.paste(corner.rotate(270), (width - radius, 0))
    return rectangle