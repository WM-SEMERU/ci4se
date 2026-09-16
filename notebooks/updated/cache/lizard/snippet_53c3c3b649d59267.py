def download_image(image_id, url, x1, y1, x2, y2, output_dir):
    output_filename = os.path.join(output_dir, image_id + '.png')
    if os.path.exists(output_filename):
        return True
    try:
        url_file = urlopen(url)
        if url_file.getcode() != 200:
            return False
        image_buffer = url_file.read()
        image = Image.open(BytesIO(image_buffer)).convert('RGB')
        w = image.size[0]
        h = image.size[1]
        image = image.crop((int(x1 * w), int(y1 * h), int(x2 * w), int(y2 * h))
            )
        image = image.resize((299, 299), resample=Image.ANTIALIAS)
        image.save(output_filename)
    except IOError:
        return False
    return True