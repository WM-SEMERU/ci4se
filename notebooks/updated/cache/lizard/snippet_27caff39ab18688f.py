def get_sentences_and_token_nodes(self):
    token_nodes = []
    if self.ignore_sentence_annotations:
        mp = self.mmax_project
        layer_dict = mp.annotations['sentence']
        file_id = self.get_file_id(self.name)
        sentence_anno_file = os.path.join(mp.project_path, mp.paths[
            'markable'], file_id + layer_dict['file_extension'])
        tree = etree.parse(sentence_anno_file)
        root = tree.getroot()
        sentence_root_nodes = []
        for markable in root.iterchildren():
            sentence_root_nodes.append(markable.attrib['id'])
            sentence_token_nodes = []
            for token_id in spanstring2tokens(self, markable.attrib['span']):
                if token_id in self.tokens:
                    sentence_token_nodes.append(token_id)
                    self.add_node(markable.attrib['id'], layers={self.ns, 
                        self.ns + ':sentence'})
            token_nodes.append(sentence_token_nodes)
    else:
        sentence_root_nodes = list(select_nodes_by_layer(self, self.ns +
            ':sentence'))
        for sent_node in sentence_root_nodes:
            sentence_token_nodes = []
            for token_id in self.get_token_nodes_from_sentence(sent_node):
                if token_id in self.tokens:
                    sentence_token_nodes.append(token_id)
            token_nodes.append(sentence_token_nodes)
    return sentence_root_nodes, token_nodes