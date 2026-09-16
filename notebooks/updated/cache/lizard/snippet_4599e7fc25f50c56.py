def itemData(self, item, column, role=Qt.DisplayRole):
    if role == Qt.DecorationRole:
        if column == self.COL_DECORATION:
            return item.decoration
    elif role == Qt.FontRole:
        return item.font
    elif role == Qt.ForegroundRole:
        return item.foregroundBrush
    elif role == Qt.BackgroundRole:
        return item.backgroundBrush
    elif role == Qt.SizeHintRole:
        return self.cellSizeHint if item.sizeHint is None else item.sizeHint
    return None