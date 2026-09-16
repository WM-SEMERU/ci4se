def request(self, cmds):
    if isinstance(cmds, list):
        cmd = '\n'.join(cmds)
    elif isinstance(cmds, str) or isinstance(cmds, unicode):
        cmd = cmds
    node = etree.Element(qualify('CLI', BASE_NS_1_0))
    etree.SubElement(node, qualify('Execution', BASE_NS_1_0)).text = cmd
    return self._request(node)