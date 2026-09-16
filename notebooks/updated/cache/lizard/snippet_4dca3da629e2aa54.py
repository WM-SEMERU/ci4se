def on_security_data_node(self, node):
    sid = XmlHelper.get_child_value(node, 'security')
    farr = node.GetElement('fieldData')
    dmap = defaultdict(list)
    for i in range(farr.NumValues):
        pt = farr.GetValue(i)
        [dmap[f].append(XmlHelper.get_child_value(pt, f, allow_missing=1)) for
            f in ['date'] + self.fields]
    idx = dmap.pop('date')
    frame = DataFrame(dmap, columns=self.fields, index=idx)
    frame.index.name = 'date'
    self.response[sid] = frame