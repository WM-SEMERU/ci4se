def move_conversations(self, ids, folder):
    str_ids = self._return_comma_list(ids)
    self.request('ConvAction', {'action': {'op': 'move', 'id': str_ids, 'l':
        str(folder)}})