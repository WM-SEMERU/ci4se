def to_xml(self):
    for n, v in {'method': self.method, 'status': self.status, 'date': self
        .date}.items():
        if is_empty_or_none(v):
            raise DeliveryMethodError(
                "'%s' attribute cannot be empty or None." % n)
    doc = Document()
    root = doc.createElement('delivery')
    super(DeliveryMethod, self).to_xml(root)
    self._create_text_node(root, 'method', self.method)
    self._create_text_node(root, 'status', self.status)
    self._create_text_node(root, 'reference', self.ref, True)
    self._create_text_node(root, 'date', self.date)
    return root