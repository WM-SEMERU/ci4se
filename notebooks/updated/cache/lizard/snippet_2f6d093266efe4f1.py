def on_all_ok(self):
    out_ddb = self.merge_ddb_files()
    return self.Results(node=self, returncode=0, message='DDB merge done')