def get_relative_path_from_img_id(img_id, variant_label=None, ext=None,
    create_dirs=False):
    profile, base_name = img_id.split(':', 1)
    conf = get_profile_configs(profile)
    if not variant_label:
        status_suffix = dju_settings.DJU_IMG_UPLOAD_MAIN_SUFFIX
    else:
        status_suffix = dju_settings.DJU_IMG_UPLOAD_VARIANT_SUFFIX
    name, file_ext = os.path.splitext(base_name)
    prefix = ''
    if name.startswith(dju_settings.DJU_IMG_UPLOAD_TMP_PREFIX):
        name = name[len(dju_settings.DJU_IMG_UPLOAD_TMP_PREFIX):]
        prefix = dju_settings.DJU_IMG_UPLOAD_TMP_PREFIX
    name_parts = name.split('_', 2)
    name = '{name}{status_suffix}{hash}'.format(name=name, status_suffix=
        status_suffix, hash=get_hash('_'.join(name_parts[:2]),
        variant_label=variant_label))
    if variant_label:
        name += '_' + variant_label
    if ext:
        file_ext = ext
    elif variant_label:
        for var_conf in conf['VARIANTS']:
            var_conf_label = var_conf['LABEL'] or get_variant_label(var_conf)
            if var_conf_label == variant_label:
                if var_conf['FORMAT']:
                    file_ext = var_conf['FORMAT'].lower()
                break
    if file_ext and not file_ext.startswith('.'):
        file_ext = '.' + file_ext
    relative_path = os.path.join(dju_settings.DJU_IMG_UPLOAD_SUBDIR, conf[
        'PATH'], name_parts[0][-2:], prefix + name + file_ext).replace('\\',
        '/')
    if create_dirs:
        path = media_path(relative_path)
        make_dirs_for_file_path(path, mode=dju_settings.DJU_IMG_CHMOD_DIR)
    return relative_path