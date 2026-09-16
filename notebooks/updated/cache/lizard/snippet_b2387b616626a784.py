def _execute_on_selected(self, p_cmd_str, p_execute_signal):
    try:
        todo = self.listbox.focus.todo
        todo_id = str(self.view.todolist.number(todo))
        urwid.emit_signal(self, p_execute_signal, p_cmd_str, todo_id)
        if p_cmd_str.startswith('edit'):
            urwid.emit_signal(self, 'refresh')
    except AttributeError:
        pass