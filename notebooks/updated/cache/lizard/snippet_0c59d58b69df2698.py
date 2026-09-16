def _get_logger_file_handles(self):
    handles = []
    for handler in self.logger.handlers:
        for attr in ['sock', 'socket', 'stream']:
            try:
                handle = getattr(handler, attr)
                if handle:
                    handles.append(handle)
                break
            except AttributeError:
                continue
    return handles