def append_row(self, values, value_input_option='RAW'):
    params = {'valueInputOption': value_input_option}
    body = {'values': [values]}
    return self.spreadsheet.values_append(self.title, params, body)