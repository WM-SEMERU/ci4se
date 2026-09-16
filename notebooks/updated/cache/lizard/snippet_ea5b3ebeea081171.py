def get_action(self, parent, undo_stack: QUndoStack, sel_range, protocol:
    ProtocolAnalyzer, view: int):
    min_row, max_row, start, end = sel_range
    if min_row == -1 or max_row == -1 or start == -1 or end == -1:
        return None
    if max_row != min_row:
        return None
    end = protocol.convert_index(end, view, 0, True, message_indx=min_row)[0]
    self.command = MessageBreakAction(protocol, max_row, end)
    action = QAction(self.command.text(), parent)
    action.triggered.connect(self.action_triggered)
    self.undo_stack = undo_stack
    return action