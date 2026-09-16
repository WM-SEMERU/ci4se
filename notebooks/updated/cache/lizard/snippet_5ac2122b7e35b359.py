def cvtToBlocks(rh, diskSize):
    rh.printSysLog('Enter generalUtils.cvtToBlocks')
    blocks = 0
    results = {'overallRC': 0, 'rc': 0, 'rs': 0, 'errno': 0}
    blocks = diskSize.strip().upper()
    lastChar = blocks[-1]
    if lastChar == 'G' or lastChar == 'M':
        byteSize = blocks[:-1]
        if byteSize == '':
            msg = msgs.msg['0200'][1] % (modId, blocks)
            rh.printLn('ES', msg)
            results = msgs.msg['0200'][0]
        else:
            try:
                if lastChar == 'M':
                    blocks = float(byteSize) * 1024 * 1024 / 512
                elif lastChar == 'G':
                    blocks = float(byteSize) * 1024 * 1024 * 1024 / 512
                blocks = str(int(math.ceil(blocks)))
            except Exception:
                msg = msgs.msg['0201'][1] % (modId, byteSize)
                rh.printLn('ES', msg)
                results = msgs.msg['0201'][0]
    elif blocks.strip('1234567890'):
        msg = msgs.msg['0202'][1] % (modId, blocks)
        rh.printLn('ES', msg)
        results = msgs.msg['0202'][0]
    rh.printSysLog('Exit generalUtils.cvtToBlocks, rc: ' + str(results[
        'overallRC']))
    return results, blocks