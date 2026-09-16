def disconnect(self):
    self.logger.info('DISCONNECT')
    if self.sock == NC.INVALID_SOCKET:
        return NC.ERR_NO_CONN
    self.state = NC.CS_DISCONNECTING
    ret = self.send_disconnect()
    ret2, bytes_written = self.packet_write()
    self.socket_close()
    return ret