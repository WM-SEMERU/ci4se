def collect_gallery_files(examples_dirs):
    files = []
    for example_dir in examples_dirs:
        for root, dirnames, filenames in os.walk(example_dir):
            for filename in filenames:
                if filename.endswith('.py'):
                    files.append(os.path.join(root, filename))
    return files