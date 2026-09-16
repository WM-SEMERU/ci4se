def get(self):
    return self.render('index.html', databench_version=DATABENCH_VERSION,
        meta_infos=self.meta_infos(), **self.info)