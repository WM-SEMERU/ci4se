def main(args):
    urls = []
    with open(args.file) as iF:
        urls = iF.read().splitlines()
    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)
    zeronets = []
    for i, url in enumerate(urls):
        zeronets.append((url, i + 1, len(urls), args.output_folder, args.
            overwrite))
    if args.threads <= 0 or args.threads > len(zeronets):
        nThreads = len(zeronets)
    else:
        nThreads = args.threads
    pool = Pool(nThreads)
    poolResults = pool.map(multi_run_wrapper, zeronets)
    pool.close()