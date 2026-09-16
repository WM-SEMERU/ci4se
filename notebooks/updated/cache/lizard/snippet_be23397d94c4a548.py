def initWithDelegate_port_protocol_(self, cb_obj, port, proto):
    self = super(_ChannelServerEventListener, self).init()
    if cb_obj is None:
        raise TypeError('callback object is None')
    self.__cb_obj = cb_obj
    self.__usernotif = None
    if proto == _lightbluecommon.RFCOMM:
        usernotif = (_IOBluetooth.IOBluetoothRFCOMMChannel.
            registerForChannelOpenNotifications_selector_withChannelID_direction_
            (self, 'newChannelOpened:channel:', port, _macutil.
            kIOBluetoothUserNotificationChannelDirectionIncoming))
    elif proto == _lightbluecommon.L2CAP:
        usernotif = (_IOBluetooth.IOBluetoothL2CAPChannel.
            registerForChannelOpenNotifications_selector_withPSM_direction_
            (self, 'newChannelOpened:channel:', port, _macutil.
            kIOBluetoothUserNotificationChannelDirectionIncoming))
    if usernotif is None:
        raise _socket.error('Unable to register for channel-' + 
            'opened notifications on server socket on channel/PSM %d' % port)
    self.__usernotif = usernotif
    return self