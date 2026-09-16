def _open_worksheet(self, xlsx_file):
    workbook = Workbook(xlsx_file, {'in_memory': True})
    worksheet = workbook.add_worksheet()
    yield workbook, worksheet
    workbook.close()