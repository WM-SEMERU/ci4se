def save(self, **kwargs):
    if self.output_path:
        write_ipynb(self.nb, self.output_path)