def copy(self):
    if not self.selectedIndexes():
        return
    row_min, row_max, col_min, col_max = get_idx_rect(self.selectedIndexes())
    index = header = False
    df = self.model().df
    obj = df.iloc[slice(row_min, row_max + 1), slice(col_min, col_max + 1)]
    output = io.StringIO()
    obj.to_csv(output, sep='\t', index=index, header=header)
    if not PY2:
        contents = output.getvalue()
    else:
        contents = output.getvalue().decode('utf-8')
    output.close()
    clipboard = QApplication.clipboard()
    clipboard.setText(contents)