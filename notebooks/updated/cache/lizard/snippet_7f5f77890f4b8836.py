def append_row(table, label, data):
    count = table.rowCount()
    table.insertRow(table.rowCount())
    items = QTableWidgetItem(label)
    variant = data,
    items.setData(Qt.UserRole, variant)
    table.setItem(count, 0, items)
    table.setItem(count, 1, QTableWidgetItem(data['status']))