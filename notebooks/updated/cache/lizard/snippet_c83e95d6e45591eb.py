def call_learn_bpe(workspace_dir: str, source_fname: str, target_fname: str,
    model_fname: str, num_ops: int=32000):
    learn_bpe_fname = os.path.join(workspace_dir, DIR_THIRD_PARTY,
        SUBWORD_NMT_DEST, 'learn_bpe.py')
    with bin_open(source_fname) as src_in, bin_open(target_fname
        ) as trg_in, open(model_fname, 'wb') as out:
        learn_bpe = subprocess.Popen([sys.executable, learn_bpe_fname, '-s',
            str(num_ops)], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        learn_bpe_thread = threading.Thread(target=copy_out, args=(
            learn_bpe.stdout, out))
        learn_bpe_thread.start()
        for inp in (src_in, trg_in):
            for line in inp:
                learn_bpe.stdin.write(line)
        learn_bpe.stdin.close()
        learn_bpe_thread.join()
        learn_bpe.wait()