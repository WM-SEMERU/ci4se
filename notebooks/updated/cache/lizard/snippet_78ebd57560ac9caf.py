def pst_from_io_files(tpl_files, in_files, ins_files, out_files,
    pst_filename=None):
    warnings.warn(
        'pst_from_io_files has moved to pyemu.helpers and is also ' +
        'now avaiable as a Pst class method (Pst.from_io_files())',
        PyemuWarning)
    from pyemu import helpers
    return helpers.pst_from_io_files(tpl_files=tpl_files, in_files=in_files,
        ins_files=ins_files, out_files=out_files, pst_filename=pst_filename)