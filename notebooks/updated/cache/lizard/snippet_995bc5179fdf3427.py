def send(colors, cache_dir=CACHE_DIR, to_send=True, vte_fix=False):
    if OS == 'Darwin':
        tty_pattern = '/dev/ttys00[0-9]*'
    else:
        tty_pattern = '/dev/pts/[0-9]*'
    sequences = create_sequences(colors, vte_fix)
    if to_send:
        for term in glob.glob(tty_pattern):
            util.save_file(sequences, term)
    util.save_file(sequences, os.path.join(cache_dir, 'sequences'))
    logging.info('Set terminal colors.')