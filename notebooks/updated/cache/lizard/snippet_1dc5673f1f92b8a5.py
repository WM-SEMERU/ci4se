def scroll_to_end_horizontally(self, steps=10, *args, **selectors):
    return self.device(**selectors).scroll.horiz.toEnd(steps=steps)