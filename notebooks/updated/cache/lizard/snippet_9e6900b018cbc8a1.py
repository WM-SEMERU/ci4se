def update_task_ids(self, encoder_vocab_size):
    for idx, task in enumerate(self.task_list):
        task.set_task_id(idx + encoder_vocab_size)
        tf.logging.info('Task %d (%s) has id %d.' % (idx, task.name, task.
            task_id))