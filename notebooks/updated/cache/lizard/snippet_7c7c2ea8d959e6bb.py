def remove(self, rel_path, propagate=False):
    repo_path = os.path.join(self.cache_dir, rel_path)
    c = self.database.cursor()
    c.execute('DELETE FROM  files WHERE path = ?', (rel_path,))
    if os.path.exists(repo_path):
        os.remove(repo_path)
    self.database.commit()
    if self.upstream and propagate:
        self.upstream.remove(rel_path, propagate)