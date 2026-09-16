def write_tree(zipf, src_directory, dst_directory):
    if not os.path.exists(src_directory):
        abort('Tree ' + src_directory + ' does not exist.')
    for root, _, files in os.walk(src_directory):
        for filename in files:
            if not filename.endswith(('.py', '.pem')):
                continue
            fullname = os.path.join(root, filename)
            arcname = fullname.replace(src_directory, dst_directory)
            zipf.write(fullname, arcname=arcname)