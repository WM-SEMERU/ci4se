def _process_mark_toggle(self, p_todo_id, p_force=None):
    if p_force in ['mark', 'unmark']:
        action = p_force
    else:
        action = 'mark' if p_todo_id not in self.marked_todos else 'unmark'
    if action == 'mark':
        self.marked_todos.add(p_todo_id)
        return True
    else:
        self.marked_todos.remove(p_todo_id)
        return False