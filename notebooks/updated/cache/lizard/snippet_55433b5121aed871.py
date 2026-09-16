def fire_running(self, running):
    load = {'id': self.opts['id'], 'events': [], 'cmd': '_minion_event'}
    for stag in sorted(running, key=lambda k: running[k].get('__run_num__', 0)
        ):
        if running[stag]['result'] and not running[stag]['changes']:
            continue
        tag = 'state_{0}_{1}'.format(six.text_type(running[stag]['result']),
            'True' if running[stag]['changes'] else 'False')
        load['events'].append({'tag': tag, 'data': running[stag]})
    channel = salt.transport.client.ReqChannel.factory(self.opts)
    try:
        channel.send(load)
    except Exception:
        pass
    finally:
        channel.close()
    return True