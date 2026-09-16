def fpn_map_rois_to_levels(boxes):
    sqrtarea = tf.sqrt(tf_area(boxes))
    level = tf.cast(tf.floor(4 + tf.log(sqrtarea * (1.0 / 224) + 1e-06) * (
        1.0 / np.log(2))), tf.int32)
    level_ids = [tf.where(level <= 2), tf.where(tf.equal(level, 3)), tf.
        where(tf.equal(level, 4)), tf.where(level >= 5)]
    level_ids = [tf.reshape(x, [-1], name='roi_level{}_id'.format(i + 2)) for
        i, x in enumerate(level_ids)]
    num_in_levels = [tf.size(x, name='num_roi_level{}'.format(i + 2)) for i,
        x in enumerate(level_ids)]
    add_moving_summary(*num_in_levels)
    level_boxes = [tf.gather(boxes, ids) for ids in level_ids]
    return level_ids, level_boxes