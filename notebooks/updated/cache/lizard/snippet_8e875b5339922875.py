def overlaps(self, box, th=0.0001):
    int_box = Box.intersection_box(self, box)
    small_box = self if self.smaller(box) else box
    return True if int_box.area() / small_box.area() >= th else False