def _divide_widths(self, cli, width):
    if not self.children:
        return []
    given_dimensions = self.get_dimensions(cli
        ) if self.get_dimensions else None

    def get_dimension_for_child(c, index):
        if given_dimensions and given_dimensions[index] is not None:
            return given_dimensions[index]
        else:
            return c.preferred_width(cli, width)
    dimensions = [get_dimension_for_child(c, index) for index, c in
        enumerate(self.children)]
    sum_dimensions = sum_layout_dimensions(dimensions)
    if sum_dimensions.min > width:
        return
    sizes = [d.min for d in dimensions]
    child_generator = take_using_weights(items=list(range(len(dimensions))),
        weights=[d.weight for d in dimensions])
    i = next(child_generator)
    while sum(sizes) < min(width, sum_dimensions.preferred):
        if sizes[i] < dimensions[i].preferred:
            sizes[i] += 1
        i = next(child_generator)
    while sum(sizes) < min(width, sum_dimensions.max):
        if sizes[i] < dimensions[i].max:
            sizes[i] += 1
        i = next(child_generator)
    return sizes