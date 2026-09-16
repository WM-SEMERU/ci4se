def _get_full_block(grouped_dicoms):
    data_blocks = []
    for index in range(0, len(grouped_dicoms)):
        logger.info('Creating block %s of %s' % (index + 1, len(
            grouped_dicoms)))
        data_blocks.append(_timepoint_to_block(grouped_dicoms[index]))
    size_x = numpy.shape(data_blocks[0])[0]
    size_y = numpy.shape(data_blocks[0])[1]
    size_z = numpy.shape(data_blocks[0])[2]
    size_t = len(data_blocks)
    full_block = numpy.zeros((size_x, size_y, size_z, size_t), dtype=
        data_blocks[0].dtype)
    for index in range(0, size_t):
        if full_block[:, :, :, (index)].shape != data_blocks[index].shape:
            logger.warning(
                'Missing slices (slice count mismatch between timepoint %s and %s)'
                 % (index - 1, index))
            logger.warning(
                '---------------------------------------------------------')
            logger.warning(full_block[:, :, :, (index)].shape)
            logger.warning(data_blocks[index].shape)
            logger.warning(
                '---------------------------------------------------------')
            raise ConversionError('MISSING_DICOM_FILES')
        full_block[:, :, :, (index)] = data_blocks[index]
    return full_block