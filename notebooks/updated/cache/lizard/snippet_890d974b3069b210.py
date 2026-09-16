def onExpandKeyEvent(self, keyEvent):
    if self._start is None:
        currentBlockText = self._qpart.textCursor().block().text()
        line = self._qpart.cursorPosition[0]
        visibleColumn = self._realToVisibleColumn(currentBlockText, self.
            _qpart.cursorPosition[1])
        self._start = line, visibleColumn
    modifiersWithoutAltShift = keyEvent.modifiers() & ~(Qt.AltModifier | Qt
        .ShiftModifier)
    newEvent = QKeyEvent(keyEvent.type(), keyEvent.key(),
        modifiersWithoutAltShift, keyEvent.text(), keyEvent.isAutoRepeat(),
        keyEvent.count())
    self._qpart.cursorPositionChanged.disconnect(self._reset)
    self._qpart.selectionChanged.disconnect(self._reset)
    super(self._qpart.__class__, self._qpart).keyPressEvent(newEvent)
    self._qpart.cursorPositionChanged.connect(self._reset)
    self._qpart.selectionChanged.connect(self._reset)