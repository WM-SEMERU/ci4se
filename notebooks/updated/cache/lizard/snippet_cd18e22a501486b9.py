def dragEnterEvent(self, event):
    data = event.mimeData()
    if data.hasFormat('application/x-orb-table') and data.hasFormat(
        'application/x-orb-query'):
        tableName = self.tableTypeName()
        if nstr(data.data('application/x-orb-table')) == tableName:
            event.acceptProposedAction()
            return
    elif data.hasFormat('application/x-orb-records'):
        event.acceptProposedAction()
        return
    super(XOrbRecordBox, self).dragEnterEvent(event)