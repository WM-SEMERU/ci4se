def _read_loop_websocket(self):
    while self.state == 'connected':
        p = None
        try:
            p = self.ws.recv()
        except websocket.WebSocketConnectionClosedException:
            self.logger.warning('WebSocket connection was closed, aborting')
            self.queue.put(None)
            break
        except Exception as e:
            self.logger.info('Unexpected error "%s", aborting', str(e))
            self.queue.put(None)
            break
        if isinstance(p, six.text_type):
            p = p.encode('utf-8')
        pkt = packet.Packet(encoded_packet=p)
        self._receive_packet(pkt)
    self.logger.info('Waiting for write loop task to end')
    self.write_loop_task.join()
    self.logger.info('Waiting for ping loop task to end')
    self.ping_loop_event.set()
    self.ping_loop_task.join()
    if self.state == 'connected':
        self._trigger_event('disconnect', run_async=False)
        try:
            connected_clients.remove(self)
        except ValueError:
            pass
        self._reset()
    self.logger.info('Exiting read loop task')