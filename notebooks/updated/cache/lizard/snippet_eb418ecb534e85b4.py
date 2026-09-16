def run_dssp(pdb, path=True):
    if not path:
        if isinstance(pdb, str):
            pdb = pdb.encode()
        with tempfile.NamedTemporaryFile() as temp_pdb:
            temp_pdb.write(pdb)
            temp_pdb.seek(0)
            dssp_out = subprocess.check_output(['mkdssp', temp_pdb.name])
    else:
        dssp_out = subprocess.check_output(['mkdssp', pdb])
    dssp_out = dssp_out.decode()
    return dssp_out