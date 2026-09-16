def get_baudrate_message(baudrate):
    baudrate_msgs = {Baudrate.BAUD_AUTO: 'auto baudrate', Baudrate.
        BAUD_10kBit: '10 kBit/sec', Baudrate.BAUD_20kBit: '20 kBit/sec',
        Baudrate.BAUD_50kBit: '50 kBit/sec', Baudrate.BAUD_100kBit:
        '100 kBit/sec', Baudrate.BAUD_125kBit: '125 kBit/sec', Baudrate.
        BAUD_250kBit: '250 kBit/sec', Baudrate.BAUD_500kBit: '500 kBit/sec',
        Baudrate.BAUD_800kBit: '800 kBit/sec', Baudrate.BAUD_1MBit:
        '1 MBit/s', Baudrate.BAUD_USE_BTREX: 'BTR Ext is used'}
    return baudrate_msgs.get(baudrate, 'BTR is unknown (user specific)')