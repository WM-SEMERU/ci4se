def to_kaf(self):
    if self.type == 'NAF':
        for node in self.__get_entity_nodes():
            node.set('eid', node.get('id'))
            del node.attrib['id']