def _handle_dot(self):
    self.printer = DotPrinter(self.todolist)
    try:
        arg = self.argument(1)
        todo = self.todolist.todo(arg)
        arg = self.argument(1)
        todos = set([self.todolist.todo(arg)])
        todos |= set(self.todolist.children(todo))
        todos |= set(self.todolist.parents(todo))
        todos = sorted(todos, key=lambda t: t.text())
        self.out(self.printer.print_list(todos))
    except InvalidTodoException:
        self.error('Invalid todo number given.')
    except InvalidCommandArgument:
        self.error(self.usage())