def generate_image_from_url(url=None, timeout=30):
    file_name = posixpath.basename(url)
    img_tmp = NamedTemporaryFile(delete=True)
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except Exception as e:
        return None, None
    img_tmp.write(response.content)
    img_tmp.flush()
    image = File(img_tmp)
    image.seek(0)
    return file_name, image