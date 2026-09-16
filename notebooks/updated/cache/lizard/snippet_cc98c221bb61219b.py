def get_start_stops(transcript_sequence, start_codons=None, stop_codons=None):
    transcript_sequence = transcript_sequence.upper()
    if not start_codons:
        start_codons = ['ATG']
    if not stop_codons:
        stop_codons = ['TAA', 'TAG', 'TGA']
    seq_frames = {(1): {'starts': [], 'stops': []}, (2): {'starts': [],
        'stops': []}, (3): {'starts': [], 'stops': []}}
    for codons, positions in ((start_codons, 'starts'), (stop_codons, 'stops')
        ):
        if len(codons) > 1:
            pat = re.compile('|'.join(codons))
        else:
            pat = re.compile(codons[0])
        for m in re.finditer(pat, transcript_sequence):
            start = m.start() + 1
            rem = start % 3
            if rem == 1:
                seq_frames[1][positions].append(start)
            elif rem == 2:
                seq_frames[2][positions].append(start)
            elif rem == 0:
                seq_frames[3][positions].append(start)
    return seq_frames