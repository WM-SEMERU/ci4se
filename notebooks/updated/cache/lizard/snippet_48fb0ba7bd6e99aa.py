def setup_tmpltbank_without_frames(workflow, output_dir, tags=None,
    independent_ifos=False, psd_files=None):
    if tags is None:
        tags = []
    cp = workflow.cp
    ifos = workflow.ifos
    fullSegment = workflow.analysis_time
    tmplt_bank_exe = os.path.basename(cp.get('executables', 'tmpltbank'))
    if tmplt_bank_exe == 'lalapps_tmpltbank':
        errMsg = 'Lalapps_tmpltbank cannot be used to generate template banks '
        errMsg += 'without using frames. Try another code.'
        raise ValueError(errMsg)
    exe_instance = select_tmpltbank_class(tmplt_bank_exe)
    tmplt_banks = FileList([])
    if independent_ifos:
        ifoList = [ifo for ifo in ifos]
    else:
        ifoList = [[ifo for ifo in ifos]]
    if cp.has_option_tags('workflow-tmpltbank', 'tmpltbank-write-psd-file',
        tags):
        exe_instance.write_psd = True
    else:
        exe_instance.write_psd = False
    for ifo in ifoList:
        job_instance = exe_instance(workflow.cp, 'tmpltbank', ifo=ifo,
            out_dir=output_dir, tags=tags, psd_files=psd_files)
        node = job_instance.create_nodata_node(fullSegment)
        workflow.add_node(node)
        tmplt_banks += node.output_files
    return tmplt_banks