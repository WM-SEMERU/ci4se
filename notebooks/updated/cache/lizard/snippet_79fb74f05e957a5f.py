def upload_segmentation_image_file(self, mapobject_type_name, plate_name,
    well_name, well_pos_y, well_pos_x, tpoint, zplane, filename):
    logger.info('upload segmentation image file "%s"', filename)
    if not filename.lower().endswith('png'):
        raise IOError('Filename must have "png" extension.')
    filename = os.path.expanduser(os.path.expandvars(filename))
    image = cv2.imread(filename, cv2.IMREAD_UNCHANGED | cv2.IMREAD_ANYDEPTH)
    self._upload_segmentation_image(mapobject_type_name, plate_name,
        well_name, well_pos_y, well_pos_x, tpoint, zplane, image.astype(np.
        int32))