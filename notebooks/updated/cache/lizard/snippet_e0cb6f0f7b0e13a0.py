def ReadFD(self, Channel):
    try:
        if platform.system() == 'Darwin':
            msg = TPCANMsgFDMac()
        else:
            msg = TPCANMsgFD()
        timestamp = TPCANTimestampFD()
        res = self.__m_dllBasic.CAN_ReadFD(Channel, byref(msg), byref(
            timestamp))
        return TPCANStatus(res), msg, timestamp
    except:
        logger.error('Exception on PCANBasic.ReadFD')
        raise