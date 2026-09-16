def build_blast_db_from_fasta_path(fasta_path, is_protein=False, output_dir
    =None, HALT_EXEC=False):
    fasta_dir, fasta_filename = split(fasta_path)
    if not output_dir:
        output_dir = fasta_dir or '.'
        fasta_path = fasta_filename
    if not output_dir.endswith('/'):
        db_name = output_dir + '/' + fasta_filename
    else:
        db_name = output_dir + fasta_filename
    fdb = FormatDb(WorkingDir=output_dir, HALT_EXEC=HALT_EXEC)
    if is_protein:
        fdb.Parameters['-p'].on('T')
    else:
        fdb.Parameters['-p'].on('F')
    app_result = fdb(fasta_path)
    db_filepaths = []
    for v in app_result.values():
        try:
            db_filepaths.append(v.name)
        except AttributeError:
            pass
    return db_name, db_filepaths