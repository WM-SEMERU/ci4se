def get_band_structure_from_vasp_multiple_branches(dir_name, efermi=None,
    projections=False):
    if os.path.exists(os.path.join(dir_name, 'branch_0')):
        branch_dir_names = [os.path.abspath(d) for d in glob.glob(
            '{i}/branch_*'.format(i=dir_name)) if os.path.isdir(d)]
        sort_by = lambda x: int(x.split('_')[-1])
        sorted_branch_dir_names = sorted(branch_dir_names, key=sort_by)
        branches = []
        for dir_name in sorted_branch_dir_names:
            xml_file = os.path.join(dir_name, 'vasprun.xml')
            if os.path.exists(xml_file):
                run = Vasprun(xml_file, parse_projected_eigen=projections)
                branches.append(run.get_band_structure(efermi=efermi))
            else:
                warnings.warn('Skipping {}. Unable to find {}'.format(d=
                    dir_name, f=xml_file))
        return get_reconstructed_band_structure(branches, efermi)
    else:
        xml_file = os.path.join(dir_name, 'vasprun.xml')
        if os.path.exists(xml_file):
            return Vasprun(xml_file, parse_projected_eigen=projections
                ).get_band_structure(kpoints_filename=None, efermi=efermi)
        else:
            return None