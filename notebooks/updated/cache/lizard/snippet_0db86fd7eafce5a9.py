def get_can_status_message(can_status):
    status_msgs = {CanStatus.CANERR_TXMSGLOST: 'Transmit message lost',
        CanStatus.CANERR_MEMTEST: 'Memory test failed', CanStatus.
        CANERR_REGTEST: 'Register test failed', CanStatus.CANERR_QXMTFULL:
        'Transmit queue is full', CanStatus.CANERR_QOVERRUN:
        'Receive queue overrun', CanStatus.CANERR_QRCVEMPTY:
        'Receive queue is empty', CanStatus.CANERR_BUSOFF: 'Bus Off',
        CanStatus.CANERR_BUSHEAVY: 'Error Passive', CanStatus.
        CANERR_BUSLIGHT: 'Warning Limit', CanStatus.CANERR_OVERRUN:
        'Rx-buffer is full', CanStatus.CANERR_XMTFULL: 'Tx-buffer is full'}
    return 'OK' if can_status == CanStatus.CANERR_OK else ', '.join(msg for
        status, msg in status_msgs.items() if can_status & status)