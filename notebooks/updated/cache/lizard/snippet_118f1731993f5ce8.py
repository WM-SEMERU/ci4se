def max_effect_length(self):

    def max_length_iter():
        for part in self.parts:
            if part.local_obj.findSolid():
                bb = part.local_obj.findSolid().BoundingBox()
                yield abs(bb.center - self.location.origin
                    ) + bb.DiagonalLength / 2
    try:
        return max(max_length_iter())
    except ValueError as e:
        return 0