def denormalize_bboxes(bboxes, rows, cols):
    return [denormalize_bbox(bbox, rows, cols) for bbox in bboxes]