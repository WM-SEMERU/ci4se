def send_and_read(self, packet, endpoint, timeout=15):
    queue = self.get_endpoint_queue(endpoint)
    self.send_packet(packet)
    try:
        return queue.get(timeout=timeout)
    finally:
        queue.close()