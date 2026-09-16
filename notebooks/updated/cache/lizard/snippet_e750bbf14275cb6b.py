def FilesBelongToSameModule(filename_cc, filename_h):
    if not filename_cc.endswith('.cc'):
        return False, ''
    filename_cc = filename_cc[:-len('.cc')]
    if filename_cc.endswith('_unittest'):
        filename_cc = filename_cc[:-len('_unittest')]
    elif filename_cc.endswith('_test'):
        filename_cc = filename_cc[:-len('_test')]
    filename_cc = filename_cc.replace('/public/', '/')
    filename_cc = filename_cc.replace('/internal/', '/')
    if not filename_h.endswith('.h'):
        return False, ''
    filename_h = filename_h[:-len('.h')]
    if filename_h.endswith('-inl'):
        filename_h = filename_h[:-len('-inl')]
    filename_h = filename_h.replace('/public/', '/')
    filename_h = filename_h.replace('/internal/', '/')
    files_belong_to_same_module = filename_cc.endswith(filename_h)
    common_path = ''
    if files_belong_to_same_module:
        common_path = filename_cc[:-len(filename_h)]
    return files_belong_to_same_module, common_path