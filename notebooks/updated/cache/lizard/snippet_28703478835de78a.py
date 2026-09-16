def reset_table_widget(t, rowCount, colCount):
    t.reset()
    t.horizontalHeader().reset()
    t.clear()
    t.sortItems(-1)
    t.setRowCount(rowCount)
    t.setColumnCount(colCount)