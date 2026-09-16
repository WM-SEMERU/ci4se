def iou(box1, box2):
    int_box = Box.intersection_box(box1, box2)
    int_area = int_box.area()
    union_area = box1.area() + box2.area() - int_area
    result = 0.0
    if union_area > 0:
        result = float(int_area) / float(union_area)
    return result