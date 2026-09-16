def write(self, p_todos):
    todofile = codecs.open(self.path, 'w', encoding='utf-8')
    if p_todos is list:
        for todo in p_todos:
            todofile.write(str(todo))
    else:
        todofile.write(p_todos)
    todofile.write('\n')
    todofile.close()