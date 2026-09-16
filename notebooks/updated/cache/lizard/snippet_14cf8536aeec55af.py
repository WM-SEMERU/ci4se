def WriteEventBody(self, event):
    for field_name in self._fields:
        if field_name == 'datetime':
            output_value = self._FormatDateTime(event)
        else:
            output_value = self._dynamic_fields_helper.GetFormattedField(event,
                field_name)
        output_value = self._RemoveIllegalXMLCharacters(output_value)
        column_index = self._fields.index(field_name)
        self._column_widths.setdefault(column_index, 0)
        if field_name == 'datetime':
            column_width = min(self._MAX_COLUMN_WIDTH, len(self.
                _timestamp_format) + 2)
        else:
            column_width = min(self._MAX_COLUMN_WIDTH, len(output_value) + 2)
        self._column_widths[column_index] = max(self._MIN_COLUMN_WIDTH,
            self._column_widths[column_index], column_width)
        self._sheet.set_column(column_index, column_index, self.
            _column_widths[column_index])
        if field_name == 'datetime' and isinstance(output_value, datetime.
            datetime):
            self._sheet.write_datetime(self._current_row, column_index,
                output_value)
        else:
            self._sheet.write(self._current_row, column_index, output_value)
    self._current_row += 1