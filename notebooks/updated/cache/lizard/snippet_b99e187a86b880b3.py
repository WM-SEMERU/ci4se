def to_dict(self):
    body = {'tier': self.tier, 'title': self.title, 'size': self.size}
    if hasattr(self, 'address') and self.address:
        body['address'] = self.address
    if hasattr(self, 'zone') and self.zone:
        body['zone'] = self.zone
    return body