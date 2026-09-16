def do_cat(self, path):
    path = path[0]
    tmp_file_path = self.TMP_PATH + 'tmp'
    if not os.path.exists(self.TMP_PATH):
        os.makedirs(self.TMP_PATH)
    f = self.n.downloadFile(self.current_path + path, tmp_file_path)
    f = open(tmp_file_path, 'r')
    self.stdout.write(f.read())
    self.stdout.write('\n')