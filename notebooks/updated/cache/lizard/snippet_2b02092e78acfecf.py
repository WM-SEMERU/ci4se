def _calc_avg_and_last_val(self, has_no_column, sum_existing_columns):
    sum_no_columns = len(has_no_column)
    columns_left = self.ALLOWED_COLUMNS - sum_existing_columns
    if sum_no_columns == 0:
        columns_avg = columns_left
    else:
        columns_avg = int(columns_left / sum_no_columns)
    remainder = columns_left - columns_avg * sum_no_columns
    columns_for_last_element = columns_avg + remainder
    return columns_avg, columns_for_last_element