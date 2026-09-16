def _add_skyline(self, rect):
    skylineq = collections.deque([])
    for sky in self._skyline:
        if sky.right <= rect.left or sky.left >= rect.right:
            self._merge_skyline(skylineq, sky)
            continue
        if sky.left < rect.left and sky.right > rect.left:
            self._merge_skyline(skylineq, HSegment(sky.start, rect.left -
                sky.left))
            sky = HSegment(P(rect.left, sky.top), sky.right - rect.left)
        if sky.left < rect.right:
            if sky.left == rect.left:
                self._merge_skyline(skylineq, HSegment(P(rect.left, rect.
                    top), rect.width))
            if sky.right > rect.right:
                self._merge_skyline(skylineq, HSegment(P(rect.right, sky.
                    top), sky.right - rect.right))
                sky = HSegment(sky.start, rect.right - sky.left)
        if sky.left >= rect.left and sky.right <= rect.right:
            if self._waste_management and sky.top < rect.bottom:
                self._waste.add_waste(sky.left, sky.top, sky.length, rect.
                    bottom - sky.top)
        else:
            self._merge_skyline(skylineq, sky)
    self._skyline = list(skylineq)