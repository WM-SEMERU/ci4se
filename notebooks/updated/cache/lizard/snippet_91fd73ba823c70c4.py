def prepare(self, p_args):
    if self._todo_ids:
        id_position = p_args.index('{}')
        if self._multi:
            p_args[id_position:id_position + 1] = self._todo_ids
            self._operations.append(p_args)
        else:
            for todo_id in self._todo_ids:
                operation_args = p_args[:]
                operation_args[id_position] = todo_id
                self._operations.append(operation_args)
    else:
        self._operations.append(p_args)
    self._create_label()