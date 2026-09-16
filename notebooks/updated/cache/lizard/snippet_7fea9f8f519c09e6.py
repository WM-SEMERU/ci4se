def request_system_code(self):
    log.debug('request system code list')
    a, e = self.pmm[3] & 7, self.pmm[3] >> 6
    timeout = max(0.000302 * (a + 1) * 4 ** e, 0.002)
    data = self.send_cmd_recv_rsp(12, '', timeout, check_status=False)
    if len(data) != 1 + data[0] * 2:
        log.debug('insufficient data received from tag')
        raise tt3.Type3TagCommandError(tt3.DATA_SIZE_ERROR)
    return [unpack('>H', data[i:i + 2])[0] for i in range(1, len(data), 2)]