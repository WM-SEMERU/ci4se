def create_columns(self):
    reader = self._get_csv_reader()
    headings = six.next(reader)
    try:
        examples = six.next(reader)
    except StopIteration:
        examples = []
    found_fields = set()
    for i, value in enumerate(headings):
        if i >= 20:
            break
        infer_field = self.has_headings and value not in found_fields
        to_field = {'date': 'date', 'amount': 'amount', 'description':
            'description', 'memo': 'description', 'notes': 'description'}.get(
            value.lower(), '') if infer_field else ''
        if to_field:
            found_fields.add(to_field)
        TransactionCsvImportColumn.objects.update_or_create(transaction_import
            =self, column_number=i + 1, column_heading=value if self.
            has_headings else '', to_field=to_field, example=examples[i].
            strip() if examples else '')