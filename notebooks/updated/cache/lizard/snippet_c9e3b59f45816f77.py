def add(image_path, file_name=None):
    if file_name is not None:
        dst_path = os.path.join(IMG_DIR, str(Path(file_name).stem + Path(
            image_path).suffix))
    else:
        dst_path = IMG_DIR
    if os.path.isfile(image_path):
        shutil.copy2(image_path, dst_path)