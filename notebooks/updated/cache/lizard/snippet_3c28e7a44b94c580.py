def write(self, default: bool=False):
    none_type = type(None)
    if default:
        ordered_vals = ['query', 'subject', 'identity', 'length',
            'mismatches', 'gaps', 'query_start', 'query_end',
            'subject_start', 'subject_end', 'evalue', 'bitscore']
    else:
        try:
            ordered_vals = [(self.custom_fs[i] if i in self.custom_fs else
                getattr(self, i)) for i in self.fs_order]
        except TypeError:
            ordered_vals = [getattr(self, i) for i in self.fs_order]
    fstr = '\t'.join([('-' if type(i) == none_type else str(i)) for i in
        ordered_vals])
    return '{}{}'.format(fstr, os.linesep)