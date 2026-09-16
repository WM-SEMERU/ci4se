def clear(self, models=(), commit=True):
    if not models:
        if os.path.exists(self.path):
            shutil.rmtree(self.path)
    else:
        database = self._database(writable=True)
        for model in models:
            database.delete_document(TERM_PREFIXES[DJANGO_CT] +
                get_model_ct(model))
        database.close()