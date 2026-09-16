def connectionReady(self, res=None):
    self._channel = yield self._allocate_channel()
    if _pika_version < pkg_resources.parse_version('1.0.0b1'):
        extra_args = dict(all_channels=True)
    else:
        extra_args = dict(global_qos=True)
    yield self._channel.basic_qos(prefetch_count=config.conf['qos'][
        'prefetch_count'], prefetch_size=config.conf['qos']['prefetch_size'
        ], **extra_args)
    if _pika_version < pkg_resources.parse_version('1.0.0b1'):
        TwistedProtocolConnection.connectionReady(self, res)