def refinements(self):
    cmd.select('AllBSRes',
        'byres (Hydrophobic-P or HBondDonor-P or HBondAccept-P or PosCharge-P or NegCharge-P or StackRings-P or PiCatRing-P or HalogenAcc or Metal-P)'
        )
    cmd.show('sticks', 'AllBSRes')
    cmd.hide('everything', 'centroids*')
    cmd.show('nb_spheres', 'centroids*')
    if self.object_exists('Chargecenter-P') or self.object_exists(
        'Chargecenter-L'):
        cmd.hide('nonbonded', 'chargecenter*')
        cmd.show('spheres', 'chargecenter*')
        cmd.set('sphere_scale', 0.4, 'chargecenter*')
        cmd.color('yellow', 'chargecenter*')
    cmd.set('valence', 1)
    cmd.copy('%sCartoon' % self.protname, self.protname)
    cmd.show('cartoon', '%sCartoon' % self.protname)
    cmd.show('sticks', '%sCartoon' % self.protname)
    cmd.set('stick_transparency', 1, '%sCartoon' % self.protname)
    cmd.set('sphere_scale', 0.2, 'resn HOH or Water')
    cmd.set('sphere_transparency', 0.4, '!(resn HOH or Water)')
    if 'Centroids*' in cmd.get_names('selections'):
        cmd.color('grey80', 'Centroids*')
    cmd.hide('spheres', '%sCartoon' % self.protname)
    cmd.hide('cartoon', '%sCartoon and resn DA+DG+DC+DU+DT+A+G+C+U+T' %
        self.protname)
    if self.ligname == 'SF4':
        cmd.show('spheres', '%s' % self.ligname)
    cmd.hide('everything', 'resn HOH &!Water')
    cmd.hide('sticks', '%s and !%s and !AllBSRes' % (self.protname, self.
        ligname))
    if self.ligandtype in ['PEPTIDE', 'INTRA']:
        self.adapt_for_peptides()
    if self.ligandtype == 'INTRA':
        self.adapt_for_intra()