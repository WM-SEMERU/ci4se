def _maybe_download_corpus(tmp_dir, vocab_type):
    filename = os.path.basename(PTB_URL)
    compressed_filepath = generator_utils.maybe_download(tmp_dir, filename,
        PTB_URL)
    ptb_files = []
    ptb_char_files = []
    with tarfile.open(compressed_filepath, 'r:gz') as tgz:
        files = []
        for m in tgz.getmembers():
            if 'ptb' in m.name and '.txt' in m.name:
                if 'char' in m.name:
                    ptb_char_files += [m.name]
                else:
                    ptb_files += [m.name]
                files += [m]
        tgz.extractall(tmp_dir, members=files)
    if vocab_type == text_problems.VocabType.CHARACTER:
        return ptb_char_files
    else:
        return ptb_files