def convert_bank_to_hdf(workflow, xmlbank, out_dir, tags=None):
    if tags is None:
        tags = []
    if len(xmlbank) > 1:
        raise ValueError('Can only convert a single template bank')
    logging.info('convert template bank to HDF')
    make_analysis_dir(out_dir)
    bank2hdf_exe = PyCBCBank2HDFExecutable(workflow.cp, 'bank2hdf', ifos=
        workflow.ifos, out_dir=out_dir, tags=tags)
    bank2hdf_node = bank2hdf_exe.create_node(xmlbank[0])
    workflow.add_node(bank2hdf_node)
    return bank2hdf_node.output_files