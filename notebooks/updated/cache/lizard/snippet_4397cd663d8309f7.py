def pdb(self):
    header_title = '{:<80}\n'.format('HEADER    {}'.format(self.id))
    data_type = '{:<80}\n'.format('EXPDTA    ISAMBARD Model')
    pdb_strs = []
    for ampal in self:
        if isinstance(ampal, Assembly):
            pdb_str = ampal.make_pdb(header=False, footer=False)
        else:
            pdb_str = ampal.make_pdb()
        pdb_strs.append(pdb_str)
    merged_strs = 'ENDMDL\n'.join(pdb_strs) + 'ENDMDL\n'
    merged_pdb = ''.join([header_title, data_type, merged_strs])
    return merged_pdb