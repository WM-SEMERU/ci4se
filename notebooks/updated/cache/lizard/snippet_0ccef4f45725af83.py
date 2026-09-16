def image_to_base64(image):
    ax = image.axes
    binary_buffer = io.BytesIO()
    lim = ax.axis()
    ax.axis(image.get_extent())
    image.write_png(binary_buffer)
    ax.axis(lim)
    binary_buffer.seek(0)
    return base64.b64encode(binary_buffer.read()).decode('utf-8')