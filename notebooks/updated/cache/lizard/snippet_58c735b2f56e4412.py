def write_page(buf, xfer_offset):
    xfer_base = 134217728
    set_address(xfer_base + xfer_offset)
    __dev.ctrl_transfer(33, __DFU_DNLOAD, 2, __DFU_INTERFACE, buf, __TIMEOUT)
    if get_status() != __DFU_STATE_DFU_DOWNLOAD_BUSY:
        raise Exception('DFU: write memory failed')
    if get_status() != __DFU_STATE_DFU_DOWNLOAD_IDLE:
        raise Exception('DFU: write memory failed')
    if __verbose:
        print('Write: 0x%x ' % (xfer_base + xfer_offset))