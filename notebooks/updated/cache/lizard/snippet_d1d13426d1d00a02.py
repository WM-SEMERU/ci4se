def get_files_by_img_id(img_id, check_hash=True):
    main_rel_path = get_relative_path_from_img_id(img_id)
    main_path = media_path(main_rel_path)
    if not os.path.isfile(main_path):
        return None
    filename = os.path.basename(main_rel_path)
    name_left_part = filename.split(dju_settings.DJU_IMG_UPLOAD_MAIN_SUFFIX, 1
        )[0]
    img_name = name_left_part
    if img_name.startswith(dju_settings.DJU_IMG_UPLOAD_TMP_PREFIX):
        img_name = img_name[len(dju_settings.DJU_IMG_UPLOAD_TMP_PREFIX):]
    img_name_parts = img_name.split('_', 2)
    img_name = '_'.join(img_name_parts[:2])
    search_pattern = (name_left_part + dju_settings.
        DJU_IMG_UPLOAD_VARIANT_SUFFIX + '*')
    search_dir = os.path.dirname(main_path)
    variants = {}
    for var_path in glob.iglob(os.path.join(search_dir, search_pattern.
        replace('\\', '/'))):
        var_filename = os.path.basename(var_path)
        m = variant_hash_label_re.match(var_filename)
        if not m:
            continue
        var_hash, var_label = m.groups()
        if check_hash and var_hash != get_hash(img_name, var_label):
            continue
        variants[var_label] = os.path.relpath(var_path, settings.MEDIA_ROOT)
    return {'main': main_rel_path, 'variants': variants}