def delete_row(self, index):
    body = {'requests': [{'deleteDimension': {'range': {'sheetId': self.id,
        'dimension': 'ROWS', 'startIndex': index - 1, 'endIndex': index}}}]}
    return self.spreadsheet.batch_update(body)