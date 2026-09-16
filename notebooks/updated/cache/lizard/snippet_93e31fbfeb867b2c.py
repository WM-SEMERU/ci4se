def _handle_callback(self, data):
    cb_id = data.get('id')
    args = data.get('args')
    event = self.__callbacks.pop(cb_id, None)
    if not event:
        return
    if not args:
        event.put(args)
        return
    err, info = args
    if err is None:
        event.put(info)
    else:
        LOGGER.warning('Callback returned error of %s', str(err))
        event.put(err)