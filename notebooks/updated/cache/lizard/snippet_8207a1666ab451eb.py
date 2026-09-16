def show_stacking(self):
    grp = self.getPseudoBondGroup('pi-Stacking-%i' % self.tid,
        associateWith=[self.model])
    grp.lineWidth = 3
    grp.lineType = self.chimera.Dash
    for i, stack in enumerate(self.plcomplex.pistacking):
        m = self.model
        r = m.newResidue('pseudoatoms', ' ', 1, ' ')
        centroid_prot = m.newAtom('CENTROID', self.chimera.Element('CENTROID'))
        x, y, z = stack.proteinring_center
        centroid_prot.setCoord(self.chimera.Coord(x, y, z))
        r.addAtom(centroid_prot)
        centroid_lig = m.newAtom('CENTROID', self.chimera.Element('CENTROID'))
        x, y, z = stack.ligandring_center
        centroid_lig.setCoord(self.chimera.Coord(x, y, z))
        r.addAtom(centroid_lig)
        b = grp.newPseudoBond(centroid_lig, centroid_prot)
        b.color = self.colorbyname('forest green')
        self.bs_res_ids += stack.proteinring_atoms