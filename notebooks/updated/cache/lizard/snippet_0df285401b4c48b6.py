def get_subsections(srcdir, examples_dir, sortkey):
    subfolders = [subfolder for subfolder in os.listdir(examples_dir) if os
        .path.exists(os.path.join(examples_dir, subfolder, 'README.txt'))]
    base_examples_dir_path = os.path.relpath(examples_dir, srcdir)
    subfolders_with_path = [os.path.join(base_examples_dir_path, item) for
        item in subfolders]
    sorted_subfolders = sorted(subfolders_with_path, key=sortkey)
    return [subfolders[i] for i in [subfolders_with_path.index(item) for
        item in sorted_subfolders]]