def create_fa(self):
    if self._seqs is None:
        os.symlink(self._fa0_fn, self._fa_fn)
    else:
        in_seqs = pyfaidx.Fasta(self._fa0_fn)
        with open(self._fa_fn, 'w+') as g:
            for seq_desc in self._seqs:
                x = in_seqs[seq_desc]
                name, seq = x.name, str(x)
                g.write('>' + name + '\n')
                n = 80
                seq_split = '\n'.join([seq[i:i + n] for i in range(0, len(
                    seq), n)])
                g.write(seq_split + '\n')