def anchor_and_curate_genV_and_genJ(self, V_anchor_pos_file, J_anchor_pos_file
    ):
    V_anchor_pos = load_genomic_CDR3_anchor_pos_and_functionality(
        V_anchor_pos_file)
    J_anchor_pos = load_genomic_CDR3_anchor_pos_and_functionality(
        J_anchor_pos_file)
    for V in self.genV:
        try:
            if V_anchor_pos[V[0]][0] > 0 and V_anchor_pos[V[0]][1] == 'F':
                V[1] = V[2][V_anchor_pos[V[0]][0]:]
            else:
                V[1] = ''
        except KeyError:
            V[1] = ''
    for J in self.genJ:
        try:
            if J_anchor_pos[J[0]][0] > 0 and J_anchor_pos[J[0]][1] == 'F':
                J[1] = J[2][:J_anchor_pos[J[0]][0] + 3]
            else:
                J[1] = ''
        except KeyError:
            J[1] = ''