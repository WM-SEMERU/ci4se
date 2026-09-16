def disconnect(self):
    if self.connected and self.channel:
        logging.debug('Disconnecting KNX/IP tunnel...')
        frame = KNXIPFrame(KNXIPFrame.DISCONNECT_REQUEST)
        frame.body = self.hpai_body()
        if self.seq < 255:
            self.seq += 1
        else:
            self.seq = 0
        self.control_socket.sendto(bytes(frame.to_frame()), (self.remote_ip,
            self.remote_port))
    else:
        logging.debug('Disconnect - no connection, nothing to do')
    self.channel = None
    self.connected = False