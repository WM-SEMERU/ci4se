def image_post_delete_handler(sender, instance, **kwargs):
    for f in glob.glob('{}/{}*'.format(instance.image.storage.location,
        instance.image.name)):
        if not os.path.isdir(f):
            instance.image.storage.delete(f)