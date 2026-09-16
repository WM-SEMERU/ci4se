def move_attached_files_to_storage(attached_files, recID, comid):
    for filename, filepath in iteritems(attached_files):
        dest_dir = os.path.join(CFG_COMMENTSDIR, str(recID), str(comid))
        try:
            os.makedirs(dest_dir)
        except:
            pass
        shutil.move(filepath, os.path.join(dest_dir, filename))