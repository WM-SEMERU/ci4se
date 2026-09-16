def websocket_safe_read(self):
    data = ''
    while True:
        try:
            data += '{0}\n'.format(self.websocket.recv())
        except WebSocketException as e:
            if isinstance(e, WebSocketConnectionClosedException):
                logger.warning(
                    'lost websocket connection, try to reconnect now')
            else:
                logger.warning('websocket exception: %s', e)
            self.reconnect()
        except Exception as e:
            if isinstance(e, SSLError) and e.errno == 2:
                pass
            else:
                logger.warning('Exception in websocket_safe_read: %s', e)
            return data.rstrip()