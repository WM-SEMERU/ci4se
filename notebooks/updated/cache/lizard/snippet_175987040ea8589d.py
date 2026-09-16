def get_position_d(self):
    data = []
    data.append(9)
    data.append(self.servoid)
    data.append(RAM_READ_REQ)
    data.append(POSITION_KD_RAM)
    data.append(BYTE2)
    send_data(data)
    rxdata = []
    try:
        rxdata = SERPORT.read(13)
        return ord(rxdata[10]) * 256 + (ord(rxdata[9]) & 255)
    except HerkulexError:
        raise HerkulexError('could not communicate with motors')