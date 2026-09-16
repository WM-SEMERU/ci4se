def receive_datagram(self, data, address):
    if not self.app:
        logger.debug('Packet received', address, data)
        return False
    try:
        response = self.app.handle_message(data, address)
    except Exception as err:
        logger.error('Error processing message from ' + str(address) + ':' +
            str(data))
        logger.error(traceback.format_exc())
        return False
    if response:
        self.send_datagram(response, address)