def convert_to_base64(self, path):
    mime = magic.Magic(mime=True)
    content_type = mime.from_file(path)
    archive = ''
    with open(path, 'rb') as image_file:
        archive = b64encode(image_file.read())
        archive = archive.decode('utf-8')
    return 'data:' + content_type + ';base64,' + archive