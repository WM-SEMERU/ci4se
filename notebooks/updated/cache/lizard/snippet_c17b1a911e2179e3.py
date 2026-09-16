def compress(self, image_path):
    if os.path.exists(image_path):
        compressed_image = '%s.gz' % image_path
        os.system('gzip -c -6 %s > %s' % (image_path, compressed_image))
        return compressed_image
    bot.exit('Cannot find image %s' % image_path)