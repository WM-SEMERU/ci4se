def request(device, response_queue, payload, timeout_s=None, poll=POLL_QUEUES):
    device.write(payload)
    if poll:
        start = dt.datetime.now()
        while not response_queue.qsize():
            if (dt.datetime.now() - start).total_seconds() > timeout_s:
                raise queue.Empty('No response received.')
        return response_queue.get()
    else:
        return response_queue.get(timeout=timeout_s)