def GetNotificationShard(self, queue):
    queue_name = str(queue)
    QueueManager.notification_shard_counters.setdefault(queue_name, 0)
    QueueManager.notification_shard_counters[queue_name] += 1
    notification_shard_index = QueueManager.notification_shard_counters[
        queue_name] % self.num_notification_shards
    if notification_shard_index > 0:
        return queue.Add(str(notification_shard_index))
    else:
        return queue