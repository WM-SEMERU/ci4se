def _cleanup(self):
    if self.todolist.exists():
        try:
            saved_todo = iter(open(self.todolist, encoding='utf-8'))
            int(next(saved_todo).strip())
            for line in saved_todo:
                _, serial = line.strip().split()
                int(serial)
        except (StopIteration, ValueError):
            logger.info('Removing inconsistent todo list.')
            self.todolist.unlink()