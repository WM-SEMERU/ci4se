def watch_log_for_alive(self, nodes, from_mark=None, timeout=720, filename=
    'system.log'):
    super(DseNode, self).watch_log_for_alive(nodes, from_mark=from_mark,
        timeout=timeout, filename=filename)