def __Script_Editor_Output_plainTextEdit_refresh_ui(self):
    memory_handler_stack_depth = len(self.__engine.
        logging_session_handler_stream.stream)
    if memory_handler_stack_depth != self.__memory_handler_stack_depth:
        for line in self.__engine.logging_session_handler_stream.stream[self
            .__memory_handler_stack_depth:memory_handler_stack_depth]:
            self.Script_Editor_Output_plainTextEdit.moveCursor(QTextCursor.End)
            self.Script_Editor_Output_plainTextEdit.insertPlainText(line)
        self.__Script_Editor_Output_plainTextEdit_set_default_view_state()
        self.__memory_handler_stack_depth = memory_handler_stack_depth