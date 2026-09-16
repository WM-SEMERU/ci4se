def _do_cancel_problems(self):
    try:
        while True:
            item = self._cancel_queue.get()
            if item is None:
                break
            item_list = [item]
            while True:
                try:
                    item_list.append(self._cancel_queue.get_nowait())
                except queue.Empty:
                    break
            try:
                body = [item[0] for item in item_list]
                try:
                    self.session.delete(posixpath.join(self.endpoint,
                        'problems/'), json=body)
                except requests.exceptions.Timeout:
                    raise RequestTimeout
            except Exception as err:
                for _, future in item_list:
                    if future is not None:
                        future._set_error(err, sys.exc_info())
            [self._cancel_queue.task_done() for _ in item_list]
            time.sleep(0)
    except Exception as err:
        _LOGGER.exception(err)