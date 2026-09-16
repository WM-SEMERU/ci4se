def parse(self, csv_row: str):
    self.date = self.parse_euro_date(csv_row[2])
    self.symbol = csv_row[0]
    self.value = self.parse_value(csv_row[1])
    return self