def upgrade_file(path, multipoint):
    node0 = nrml.read(path, chatty=False)[0]
    shutil.copy(path, path + '.bak')
    tag = striptag(node0.tag)
    gml = True
    if tag == 'vulnerabilityModel':
        vf_dict, cat_dict = get_vulnerability_functions_04(path)
        node0 = Node('vulnerabilityModel', cat_dict, nodes=[obj_to_node(val
            ) for val in vf_dict.values()])
        gml = False
    elif tag == 'fragilityModel':
        node0 = read_nrml.convert_fragility_model_04(nrml.read(path)[0], path)
        gml = False
    elif tag == 'sourceModel':
        node0 = nrml.read(path)[0]
        dic = groupby(node0.nodes, operator.itemgetter('tectonicRegion'))
        node0.nodes = [Node('sourceGroup', dict(tectonicRegion=trt, name=
            'group %s' % i), nodes=srcs) for i, (trt, srcs) in enumerate(
            dic.items(), 1)]
        if multipoint:
            sourceconverter.update_source_model(node0, path + '.bak')
    with open(path, 'wb') as f:
        nrml.write([node0], f, gml=gml)