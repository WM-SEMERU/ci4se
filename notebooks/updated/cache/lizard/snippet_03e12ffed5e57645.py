def get_image_tar(image_path):
    bot.debug('Generate file system tar...')
    file_obj = Client.image.export(image_path=image_path)
    if file_obj is None:
        bot.error('Error generating tar, exiting.')
        sys.exit(1)
    tar = tarfile.open(file_obj)
    return file_obj, tar