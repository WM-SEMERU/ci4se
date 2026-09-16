def accept(self):
    if not self.save():
        return
    for i in range(self.uiActionTREE.topLevelItemCount()):
        item = self.uiActionTREE.topLevelItem(i)
        action = item.action()
        action.setShortcut(QKeySequence(item.text(1)))
    super(XShortcutDialog, self).accept()