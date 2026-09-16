def _to_dict(self):
    _dict = {}
    if hasattr(self, 'content') and self.content is not None:
        _dict['content'] = self.content
    if hasattr(self, 'id') and self.id is not None:
        _dict['id'] = self.id
    if hasattr(self, 'created') and self.created is not None:
        _dict['created'] = self.created
    if hasattr(self, 'updated') and self.updated is not None:
        _dict['updated'] = self.updated
    if hasattr(self, 'contenttype') and self.contenttype is not None:
        _dict['contenttype'] = self.contenttype
    if hasattr(self, 'language') and self.language is not None:
        _dict['language'] = self.language
    if hasattr(self, 'parentid') and self.parentid is not None:
        _dict['parentid'] = self.parentid
    if hasattr(self, 'reply') and self.reply is not None:
        _dict['reply'] = self.reply
    if hasattr(self, 'forward') and self.forward is not None:
        _dict['forward'] = self.forward
    return _dict