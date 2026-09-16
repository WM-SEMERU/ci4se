def pretty_emit(self, record, is_header=False, task_level=None):
    task = record.task or self.cur_task
    if task_level is None:
        task_level = self.cur_depth_level
    if is_header:
        extra_prefix = self.get_task_indicator(task_level - 1) + ' ' + ('' if
            self.am_i_main_thread else '[%s] ' % self.cur_thread) + task + ': '
        record.levelno = logging.INFO
    else:
        extra_prefix = '  ' + self.get_task_indicator(task_level) + ' '
    if task:
        record.msg = '  ' * (task_level - 1) + extra_prefix + str(record.msg)
    super().emit(record)
    super().flush()