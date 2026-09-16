def join(self, people):
    tries = 0
    if not people:
        raise SensorJoinException('No people given')
    ids = set()
    for person in people:
        if not person.id and person.id != 0:
            raise SensorJoinException('Invalid id for one or more people')
        if person.id in ids:
            raise SensorJoinException('Id {} not unique'.format(person.id))
        ids.add(person.id)
    while self._is_running and tries < self._join_retry_count:
        packet = APPJoinMessage(payload={'people': [person.to_dict() for
            person in people]})
        self._send_packet(self._multicast_group, self._multicast_port, packet)
        if self._joined.wait(self._join_retry_timeout):
            break
        with self._seq_ack_lock:
            packet_ackd = packet.header.sequence_number not in self._seq_ack
        if packet_ackd and self._joined.wait(1.0):
            break
        tries += 1
        self.warning('Unsuccessful attempt joining audience # {}'.format(tries)
            )
    if not self._joined.is_set() or tries >= self._join_retry_count:
        raise SensorJoinException('No config packet received')
    self.info('Joined the audience')