def run_dependent_peptides(allPeptides_file, rawFilesTable_file, outfile):
    __dep, localization = read_dependent_peptides(allPeptides_file)
    exp = read_rawFilesTable(rawFilesTable_file)
    _dep = _set_column_names(__dep, exp)
    main_columns = list(_dep.columns)
    dep = _dep.join(localization).reset_index()
    dep.to_perseus(outfile, main_columns=main_columns)