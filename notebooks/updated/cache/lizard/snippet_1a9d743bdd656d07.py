def write_xls(data, file_name, worksheet_names=None):
    workbook = xlwt.Workbook()
    for sheet_index, sheet_data in enumerate(data):
        if worksheet_names and sheet_index < len(worksheet_names
            ) and worksheet_names[sheet_index]:
            name = worksheet_names[sheet_index]
        else:
            name = 'Worksheet {}'.format(sheet_index)
        sheet = workbook.add_sheet(name)
        for row_index, row in enumerate(sheet_data):
            for col_index, value in enumerate(row):
                sheet.write(row_index, col_index, value)
    workbook.save(file_name)