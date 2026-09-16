def circles_pycairo(width, height, color):
    cairo_color = color / rgb(255, 255, 255)
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)
    ctx.new_path()
    ctx.set_source_rgb(cairo_color.red, cairo_color.green, cairo_color.blue)
    ctx.arc(width / 2, height / 2, width / 2, 0, 2 * pi)
    ctx.fill()
    surface.write_to_png('circles.png')