def create_png(cls_name, meth_name, graph, dir_name='graphs2'):
    m_name = ''.join(x for x in meth_name if x.isalnum())
    name = ''.join((cls_name.split('/')[-1][:-1], '#', m_name))
    graph.draw(name, dir_name)