def clean(self):
    rnftools.utils.shell('rm -fR "{}" "{}"'.format(self.report_dir, self.
        _html_fn))