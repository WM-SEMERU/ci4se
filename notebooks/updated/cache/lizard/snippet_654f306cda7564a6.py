def run_sync(self):
    while self.connected:
        try:
            self.pump_reader()
        except PacketDecodeError as e:
            logger.warning('Packet decode failed: %s', e)
        except ConnectionError:
            break