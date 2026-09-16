def build_tree_from_alignment(aln, moltype=DNA, best_tree=False, params={},
    working_dir='/tmp'):
    params['--out'] = get_tmp_filename(working_dir)
    app = Clearcut(InputHandler='_input_as_multiline_string', params=params,
        WorkingDir=working_dir, SuppressStdout=True, SuppressStderr=True)
    app.Parameters['-a'].on()
    app.Parameters['-d'].off()
    if moltype == RNA:
        moltype = DNA
    if best_tree:
        app.Parameters['-N'].on()
    moltype_string = moltype.label.upper()
    app.Parameters[MOLTYPE_MAP[moltype_string]].on()
    seq_aln = Alignment(aln, MolType=moltype)
    int_map, int_keys = seq_aln.getIntMap()
    int_map = Alignment(int_map)
    result = app(int_map.toFasta())
    tree = DndParser(result['Tree'].read(), constructor=PhyloNode)
    for node in tree.tips():
        node.Name = int_keys[node.Name]
    result.cleanUp()
    del (seq_aln, app, result, int_map, int_keys, params)
    return tree