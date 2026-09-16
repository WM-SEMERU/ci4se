def set_count(self, cnt):
    if isinstance(cnt, int) and cnt > 0 and cnt <= 100:
        self.arguments.update({'count': '%s' % cnt})
    else:
        raise TwitterSearchException(1004)