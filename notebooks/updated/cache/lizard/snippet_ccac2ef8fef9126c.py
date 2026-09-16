def update_artifact_cache(self, vts_artifactfiles_pairs):
    update_artifact_cache_work = self._get_update_artifact_cache_work(
        vts_artifactfiles_pairs)
    if update_artifact_cache_work:
        self.context.submit_background_work_chain([
            update_artifact_cache_work], parent_workunit_name='cache')