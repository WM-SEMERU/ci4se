def available():
    font_dir = os.path.dirname(__file__)
    names = [os.path.basename(os.path.splitext(f)[0]) for f in glob(os.path
        .join(font_dir, '*.pil'))]
    return sorted(names)