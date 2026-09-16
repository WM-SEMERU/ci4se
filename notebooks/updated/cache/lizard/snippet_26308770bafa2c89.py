def _get_net(self, entry):
    try:
        net = entry[1]
        return net[net.find('(') + 1:net.find(')')]
    except IndexError:
        return None