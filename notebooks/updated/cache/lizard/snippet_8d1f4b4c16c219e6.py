def output_reduce(input_file, path=True, pdb_name=None, force=False):
    if path:
        output_path = reduce_output_path(path=input_file)
    else:
        output_path = reduce_output_path(pdb_name=pdb_name)
    if output_path.exists() and not force:
        return output_path
    reduce_mmol, reduce_message = run_reduce(input_file, path=path)
    if not reduce_mmol:
        return None
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(reduce_mmol)
    return output_path