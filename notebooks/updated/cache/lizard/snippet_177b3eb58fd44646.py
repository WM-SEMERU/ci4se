def get_dimension(self):
    if self.strokes > 0:
        if self.pixel_env > 0:
            return (2 + (1 + 2 * self.pixel_env) ** 2
                ) * self.strokes * self.points_per_stroke
        else:
            return 2 * self.strokes * self.points_per_stroke
    elif self.pen_down:
        return 3 * self.points_per_stroke
    else:
        return 2 * self.points_per_stroke