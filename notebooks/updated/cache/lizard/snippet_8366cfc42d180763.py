def _maybe_connect(self, node_id):
    with self._lock:
        conn = self._conns.get(node_id)
        if conn is None:
            broker = self.cluster.broker_metadata(node_id)
            assert broker, 'Broker id %s not in current metadata' % (node_id,)
            log.debug('Initiating connection to node %s at %s:%s', node_id,
                broker.host, broker.port)
            host, port, afi = get_ip_port_afi(broker.host)
            cb = WeakMethod(self._conn_state_change)
            conn = BrokerConnection(host, broker.port, afi,
                state_change_callback=cb, node_id=node_id, **self.config)
            self._conns[node_id] = conn
        elif self._should_recycle_connection(conn):
            self._conns.pop(node_id)
            return False
        elif conn.connected():
            return True
        conn.connect()
        return conn.connected()