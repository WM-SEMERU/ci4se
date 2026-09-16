def process_xlsx(content):
    data = {}
    workbook = xlrd.open_workbook(file_contents=content)
    worksheets = [w for w in workbook.sheet_names() if not w.startswith('_')]
    for worksheet_name in worksheets:
        if worksheet_name.startswith('_'):
            continue
        worksheet = workbook.sheet_by_name(worksheet_name)
        merged_cells = worksheet.merged_cells
        if len(merged_cells):
            raise MergedCellError(worksheet.name, merged_cells)
        worksheet.name = slughifi(worksheet.name)
        headers = make_headers(worksheet)
        worksheet_data = make_worksheet_data(headers, worksheet)
        data[worksheet.name] = worksheet_data
    return data