def __initialize_ui(self):
    self.__clear_button.setCursor(Qt.ArrowCursor)
    if self.__ui_clear_image and self.__ui_clear_clicked_image:
        pixmap = QPixmap(self.__ui_clear_image)
        clicked_pixmap = QPixmap(self.__ui_clear_clicked_image)
        self.__clear_button.setIcon(QIcon(pixmap))
        self.__clear_button.setMaximumSize(pixmap.size())
        self.__clear_button.pressed.connect(functools.partial(self.
            __clear_button.setIcon, QIcon(clicked_pixmap)))
        self.__clear_button.released.connect(functools.partial(self.
            __clear_button.setIcon, QIcon(pixmap)))
    else:
        self.__clear_button.setText('Clear')
    self.__set_style_sheet()
    frame_width = self.style().pixelMetric(QStyle.PM_DefaultFrameWidth)
    self.setMinimumSize(max(self.minimumSizeHint().width(), self.
        __clear_button.sizeHint().height() + frame_width * 2), max(self.
        minimumSizeHint().height(), self.__clear_button.sizeHint().height() +
        frame_width * 2))
    self.__completer.setCaseSensitivity(Qt.CaseInsensitive)
    self.__completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
    self.__completer.setMaxVisibleItems(self.__completer_visible_items_count)