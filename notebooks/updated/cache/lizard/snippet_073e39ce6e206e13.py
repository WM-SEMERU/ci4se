def get_declaration(self):
    if self.is_opaque:
        out = '{strrep} = type opaque'.format(strrep=str(self))
    else:
        out = '{strrep} = type {struct}'.format(strrep=str(self), struct=
            self.structure_repr())
    return out