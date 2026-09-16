def get_worksheet(self, index):
    sheet_data = self.fetch_sheet_metadata()
    try:
        properties = sheet_data['sheets'][index]['properties']
        return Worksheet(self, properties)
    except (KeyError, IndexError):
        return None