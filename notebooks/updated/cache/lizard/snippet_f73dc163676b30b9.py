def upload_files(self, abspaths, relpaths, remote_objects):
    for relpath in relpaths:
        abspath = [p for p in abspaths if p[len(self.file_root):] == relpath][0
            ]
        cloud_datetime = remote_objects[relpath
            ] if relpath in remote_objects else None
        local_datetime = datetime.datetime.utcfromtimestamp(os.stat(abspath
            ).st_mtime)
        if cloud_datetime and local_datetime < cloud_datetime:
            self.skip_count += 1
            if not self.quiet:
                print('Skipped {0}: not modified.'.format(relpath))
            continue
        if relpath in remote_objects:
            self.update_count += 1
        else:
            self.create_count += 1
        self.upload_file(abspath, relpath)