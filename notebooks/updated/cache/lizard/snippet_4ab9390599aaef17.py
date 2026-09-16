def check_image_duplicates(file_list):
    master_hash = ''
    ham_dist = 0
    results = []
    print('Checking Images for duplicates (despite resizing, colours, etc) ')
    for ndx, fname in enumerate(file_list):
        img = load_image(fname)
        hsh = get_img_hash(img)
        if ndx == 0:
            master_hash = hsh
        else:
            ham_dist = hamming_distance(hsh, master_hash)
        results.append({'hsh': hsh, 'fname': fname, 'dist_to_img1': str(
            ham_dist)})
    return results