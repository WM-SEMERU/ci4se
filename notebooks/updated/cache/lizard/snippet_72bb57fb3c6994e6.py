def protein_only_and_noH(self, keep_ligands=None, force_rerun=False):
    log.debug('{}: running protein receptor isolation...'.format(self.id))
    if not self.dockprep_path:
        return ValueError('Please run dockprep')
    receptor_mol2 = op.join(self.dock_dir, '{}_receptor.mol2'.format(self.id))
    receptor_noh = op.join(self.dock_dir, '{}_receptor_noH.pdb'.format(self.id)
        )
    prly_com = op.join(self.dock_dir, 'prly.com')
    if ssbio.utils.force_rerun(flag=force_rerun, outfile=receptor_noh):
        with open(prly_com, 'w') as f:
            f.write('open {}\n'.format(self.dockprep_path))
            keep_str = 'delete ~protein'
            if keep_ligands:
                keep_ligands = ssbio.utils.force_list(keep_ligands)
                for res in keep_ligands:
                    keep_str += ' & ~:{} '.format(res)
            keep_str = keep_str.strip() + '\n'
            f.write(keep_str)
            f.write('write format mol2 0 {}\n'.format(receptor_mol2))
            f.write('delete element.H\n')
            f.write('write format pdb 0 {}\n'.format(receptor_noh))
        cmd = 'chimera --nogui {}'.format(prly_com)
        os.system(cmd)
        os.remove(prly_com)
    if ssbio.utils.is_non_zero_file(receptor_mol2
        ) and ssbio.utils.is_non_zero_file(receptor_noh):
        self.receptormol2_path = receptor_mol2
        self.receptorpdb_path = receptor_noh
        log.debug('{}: successful receptor isolation (mol2)'.format(self.
            receptormol2_path))
        log.debug('{}: successful receptor isolation (pdb)'.format(self.
            receptorpdb_path))
    else:
        log.critical('{}: protein_only_and_noH failed to run on dockprep file'
            .format(self.dockprep_path))