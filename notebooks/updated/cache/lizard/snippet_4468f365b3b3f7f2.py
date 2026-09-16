def __gen_token_anno_file(self, top_level_layer):
    base_paula_id = '{0}.{1}.tok'.format(self.corpus_name, self.name)
    paula_id = '{0}.{1}.{2}.tok_multiFeat'.format(top_level_layer, self.
        corpus_name, self.name)
    E, tree = gen_paula_etree(paula_id)
    mflist = E('multiFeatList', {XMLBASE: base_paula_id + '.xml'})
    for token_id in self.dg.tokens:
        mfeat = E('multiFeat', {XLINKHREF: '#{0}'.format(token_id)})
        token_dict = self.dg.node[token_id]
        for feature in token_dict:
            if feature not in IGNORED_TOKEN_ATTRIBS and feature.startswith(
                top_level_layer):
                mfeat.append(E('feat', {'name': feature, 'value':
                    token_dict[feature]}))
        if self.human_readable:
            mfeat.append(Comment(token_dict[self.dg.ns + ':token']))
        mflist.append(mfeat)
    tree.append(mflist)
    self.files[paula_id] = tree
    self.file2dtd[paula_id] = PaulaDTDs.multifeat
    return paula_id