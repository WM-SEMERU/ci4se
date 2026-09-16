def _build_bounding_box_lookup(bounding_box_file):
    lines = tf.gfile.FastGFile(bounding_box_file, 'r').readlines()
    images_to_bboxes = {}
    num_bbox = 0
    num_image = 0
    for l in lines:
        if l:
            parts = l.split(',')
            assert len(parts) == 5, 'Failed to parse: %s' % l
            filename = parts[0]
            xmin = float(parts[1])
            ymin = float(parts[2])
            xmax = float(parts[3])
            ymax = float(parts[4])
            box = [xmin, ymin, xmax, ymax]
            if filename not in images_to_bboxes:
                images_to_bboxes[filename] = []
                num_image += 1
            images_to_bboxes[filename].append(box)
            num_bbox += 1
    print('Successfully read %d bounding boxes across %d images.' % (
        num_bbox, num_image))
    return images_to_bboxes