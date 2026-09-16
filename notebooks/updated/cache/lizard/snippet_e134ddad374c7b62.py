def runExperiment(self, e):
    space = self.parameterSpace()
    if len(space) > 0:
        nb = self.notebook()
        ps = self._mixup(space)
        try:
            self.open()
            view = self._client.load_balanced_view()
            jobs = []
            for p in ps:
                jobs.extend(view.apply_async(lambda p: e.set(p).run(), p).
                    msg_ids)
                time.sleep(0.01)
            psjs = zip(ps, jobs)
            for p, j in psjs:
                nb.addPendingResult(p, j)
        finally:
            nb.commit()
            self.close()