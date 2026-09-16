def _write_categories(self, workbook, worksheet):
    categories = self._chart_data.categories
    num_format = workbook.add_format({'num_format': categories.number_format})
    depth = categories.depth
    for idx, level in enumerate(categories.levels):
        col = depth - idx - 1
        self._write_cat_column(worksheet, col, level, num_format)