def get_comments(self):
    if self.info is None:
        self.get_info()
    if 'comments' in self.info:
        return [structure['text'] for structure in self.info['comments'][
            'comments']]
    else:
        return []