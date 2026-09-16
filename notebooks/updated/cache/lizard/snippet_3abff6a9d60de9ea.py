def uid(self, p_todo):
    try:
        return self._todo_id_map[p_todo]
    except KeyError as ex:
        raise InvalidTodoException from ex