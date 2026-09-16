def _run_evolve(ssm_file, cnv_file, work_dir, data):
    exe = os.path.join(os.path.dirname(sys.executable), 'evolve.py')
    assert os.path.exists(exe
        ), 'Could not find evolve script for PhyloWGS runs.'
    out_dir = os.path.join(work_dir, 'evolve')
    out_file = os.path.join(out_dir, 'top_k_trees')
    if not utils.file_uptodate(out_file, cnv_file):
        with file_transaction(data, out_dir) as tx_out_dir:
            with utils.chdir(tx_out_dir):
                cmd = [sys.executable, exe, '-r', '42', ssm_file, cnv_file]
                do.run(cmd, 'Run PhyloWGS evolution')
    return out_file