def _post_run_hook(self, runtime):
    self._anat_file = self.inputs.in_file
    self._mask_file = self.aggregate_outputs(runtime=runtime).mask_file
    self._seg_files = [self._mask_file]
    self._masked = True
    NIWORKFLOWS_LOG.info(
        'Generating report for nilearn.compute_epi_mask. file "%s", and mask file "%s"'
        , self._anat_file, self._mask_file)
    return super(ComputeEPIMask, self)._post_run_hook(runtime)