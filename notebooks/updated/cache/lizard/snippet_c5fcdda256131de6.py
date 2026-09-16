def resize_image(self, data):
    image = Image.open(data)
    stream_out = BytesIO()
    width, height = image.size[:]
    if height > 50:
        width = int(width * 50 / height)
        height = 50
        image = image.resize((width, 50))
    image.save(stream_out, format='JPEG', quality=100)
    stream_out.seek(0)
    return stream_out