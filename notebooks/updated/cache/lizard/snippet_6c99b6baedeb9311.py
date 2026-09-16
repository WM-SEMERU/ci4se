def process_tls(self, data, name):
    ret = []
    try:
        lines = [x.strip() for x in data.split('\n')]
        for idx, line in enumerate(lines):
            if line == '':
                continue
            sub = self.process_host(line, name, idx)
            if sub is not None:
                ret.append(sub)
    except Exception as e:
        logger.error('Error in file processing %s : %s' % (name, e))
        self.roca.trace_logger.log(e)
    return ret