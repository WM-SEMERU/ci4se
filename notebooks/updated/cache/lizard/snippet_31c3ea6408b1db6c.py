def _align_sequences(self, input_sequences_path, output_alignment_path, threads
    ):
    logging.debug('Aligning sequences using mafft')
    cmd = 'mafft --anysymbol --thread %s --auto /dev/stdin > %s' % (threads,
        output_alignment_path)
    inputs = []
    with open(input_sequences_path) as f:
        for name, seq, _ in SequenceIO().each(f):
            inputs.append('>%s' % name)
            inputs.append(seq.replace('*', ''))
    extern.run(cmd, stdin='\n'.join(inputs))