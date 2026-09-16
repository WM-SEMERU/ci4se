def tersoff_input(self, structure, periodic=False, uc=True, *keywords):
    gin = self.keyword_line(*keywords)
    gin += self.structure_lines(structure, cell_flg=periodic, frac_flg=
        periodic, anion_shell_flg=False, cation_shell_flg=False, symm_flg=
        not uc)
    gin += self.tersoff_potential(structure)
    return gin