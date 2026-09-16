def get_members(self, name):
    grpid = re.search('(\\d+)', name).group()
    command = 'show port-channel %s all-ports' % grpid
    config = self.node.enable(command, 'text')
    return re.findall('\\b(?!Peer)Ethernet[\\d/]*\\b', config[0]['result'][
        'output'])