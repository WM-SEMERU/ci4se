def serialize(self, now=None):
    created = self.created if self.created is not None else now
    el = etree.Element(utils.lxmlns('mets') + self.subsection, ID=self.
        id_string)
    if created:
        el.set('CREATED', created)
    status = self.get_status()
    if status:
        el.set('STATUS', status)
    if self.contents:
        el.append(self.contents.serialize())
    return el