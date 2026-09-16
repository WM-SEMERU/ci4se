def recognize_byte(self, image, timeout=10):
    result = []
    alpr = subprocess.Popen(self._cmd, stdin=subprocess.PIPE, stdout=
        subprocess.PIPE, stderr=subprocess.DEVNULL)
    try:
        stdout, stderr = alpr.communicate(input=image, timeout=10)
        stdout = io.StringIO(str(stdout, 'utf-8'))
    except subprocess.TimeoutExpired:
        _LOGGER.error('Alpr process timeout!')
        alpr.kill()
        return None
    tmp_res = {}
    while True:
        line = stdout.readline()
        if not line:
            if len(tmp_res) > 0:
                result.append(tmp_res)
            break
        new_plate = self.__re_plate.search(line)
        new_result = self.__re_result.search(line)
        if new_plate and len(tmp_res) > 0:
            result.append(tmp_res)
            tmp_res = {}
            continue
        if new_result:
            try:
                tmp_res[new_result.group(1)] = float(new_result.group(2))
            except ValueError:
                continue
    _LOGGER.debug('Process alpr with result: %s', result)
    return result