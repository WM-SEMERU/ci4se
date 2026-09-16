def compare(self, range_comparison, range_objs):
    range_values = [obj.value for obj in range_objs]
    comparison_func = get_comparison_func(range_comparison)
    return comparison_func(self.value, *range_values)