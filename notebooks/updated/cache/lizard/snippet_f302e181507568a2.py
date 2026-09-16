def get_image_info_by_image_id(self, image_id):
    logger.info("getting info about provided image specified by image_id '%s'",
        image_id)
    logger.debug("image_id = '%s'", image_id)
    images = self.d.images()
    try:
        image_dict = [i for i in images if i['Id'] == image_id][0]
    except IndexError:
        logger.info('image not found')
        return None
    else:
        return image_dict