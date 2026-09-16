def cells_rt_meta_pub(workbook, sheet, row, col, pub_qty):
    logger_excel.info('enter cells_rt_meta_pub')
    col_loop = 0
    cell_data = []
    temp_sheet = workbook.sheet_by_name(sheet)
    while col_loop < pub_qty:
        col += 1
        col_loop += 1
        cell_data.append(temp_sheet.cell_value(row, col))
    logger_excel.info('exit cells_rt_meta_pub')
    return cell_data