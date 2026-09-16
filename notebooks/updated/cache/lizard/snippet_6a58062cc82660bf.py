def delete(cls, repo, path):
    full_ref_path = cls.to_full_path(path)
    abs_path = osp.join(repo.common_dir, full_ref_path)
    if osp.exists(abs_path):
        os.remove(abs_path)
    else:
        pack_file_path = cls._get_packed_refs_path(repo)
        try:
            with open(pack_file_path, 'rb') as reader:
                new_lines = []
                made_change = False
                dropped_last_line = False
                for line in reader:
                    line = line.decode(defenc)
                    if (line.startswith('#') or full_ref_path not in line
                        ) and (not dropped_last_line or dropped_last_line and
                        not line.startswith('^')):
                        new_lines.append(line)
                        dropped_last_line = False
                        continue
                    made_change = True
                    dropped_last_line = True
            if made_change:
                with open(pack_file_path, 'wb') as fd:
                    fd.writelines(l.encode(defenc) for l in new_lines)
        except (OSError, IOError):
            pass
    reflog_path = RefLog.path(cls(repo, full_ref_path))
    if osp.isfile(reflog_path):
        os.remove(reflog_path)