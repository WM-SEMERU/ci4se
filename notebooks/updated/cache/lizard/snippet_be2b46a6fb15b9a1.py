def drop_all(self, queue_name):
    task_ids = self.conn.lrange(queue_name, 0, -1)
    for task_id in task_ids:
        self.conn.delete(task_id)
    self.conn.delete(queue_name)