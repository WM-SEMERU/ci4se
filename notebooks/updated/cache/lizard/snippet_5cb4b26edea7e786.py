def write(self, destination, source_model, name=None):
    if os.path.exists(destination):
        os.remove(destination)
    self.destination = destination
    if name:
        source_model.name = name
    output_source_model = Node('sourceModel', {'name': name})
    dic = groupby(source_model.sources, operator.itemgetter('tectonicRegion'))
    for i, (trt, srcs) in enumerate(dic.items(), 1):
        output_source_model.append(Node('sourceGroup', {'tectonicRegion':
            trt, 'name': 'group %d' % i}, nodes=srcs))
    print('Exporting Source Model to %s' % self.destination)
    with open(self.destination, 'wb') as f:
        nrml.write([output_source_model], f, '%s')