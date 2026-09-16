def _get_header(self):
    try:
        header_lines = [int(e) for e in str(self.get_value('headerlines', 0
            )).split(',')]
    except ValueError as e:
        header_lines = [0]
    header_rows = islice(self.row_generator, min(header_lines), max(
        header_lines) + 1)
    from tableintuit import RowIntuiter
    headers = RowIntuiter.coalesce_headers(header_rows)
    return headers