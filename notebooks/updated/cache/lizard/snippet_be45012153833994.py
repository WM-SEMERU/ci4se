def ProcessMessages(self, active_notifications, queue_manager, time_limit=0):
    now = time.time()
    processed = 0
    for notification in active_notifications:
        if notification.session_id not in self.queued_flows:
            if time_limit and time.time() - now > time_limit:
                break
            processed += 1
            self.queued_flows.Put(notification.session_id, 1)
            self.thread_pool.AddTask(target=self._ProcessMessages, args=(
                notification, queue_manager.Copy()), name=self.__class__.
                __name__)
    return processed