def get_next_page(self):
    master_node = self._retrieve_next_page()
    seq = []
    for node in master_node.getElementsByTagName('track'):
        track = Track(_extract(node, 'artist'), _extract(node, 'name'),
            self.network, info={'image': _extract_all(node, 'image')})
        track.listener_count = _number(_extract(node, 'listeners'))
        seq.append(track)
    return seq