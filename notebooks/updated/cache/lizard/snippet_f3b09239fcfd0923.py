def version(self):
    match = re.search('(\\d+)\\.(\\d+)\\.(\\d+)', self.raw_cmd('version').
        communicate()[0].decode('utf-8'))
    return [match.group(i) for i in range(4)]