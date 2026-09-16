def move_cursor(self, chars=0):
    direction = QTextCursor.Right if chars > 0 else QTextCursor.Left
    for _i in range(abs(chars)):
        self.moveCursor(direction, QTextCursor.MoveAnchor)