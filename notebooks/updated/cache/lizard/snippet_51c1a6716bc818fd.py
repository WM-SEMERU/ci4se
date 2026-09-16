def get(img, cache_dir=CACHE_DIR, iterative=False):
    if os.path.isfile(img):
        wal_img = img
    elif os.path.isdir(img):
        if iterative:
            wal_img = get_next_image(img)
        else:
            wal_img = get_random_image(img)
    else:
        logging.error('No valid image file found.')
        sys.exit(1)
    wal_img = os.path.abspath(wal_img)
    util.save_file(wal_img, os.path.join(cache_dir, 'wal'))
    logging.info('Using image \x1b[1;37m%s\x1b[0m.', os.path.basename(wal_img))
    return wal_img