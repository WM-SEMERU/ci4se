def suspend_queues(self, active_queues, sleep_time=10.0):
    for queue in active_queues:
        self.disable_queue(queue)
    while self.get_active_tasks():
        time.sleep(sleep_time)