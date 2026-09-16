def filter(self, *LayoutClasses, **kwargs):
    self._check_layout()
    max_level = kwargs.pop('max_level', 0)
    greedy = kwargs.pop('greedy', False)
    filtered_layout_objects = self.layout.get_layout_objects(LayoutClasses,
        max_level=max_level, greedy=greedy)
    return LayoutSlice(self.layout, filtered_layout_objects)