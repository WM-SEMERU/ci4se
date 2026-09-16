def set_default_format_options(self, format_options, read=False):
    if self.default_notebook_metadata_filter:
        format_options.setdefault('notebook_metadata_filter', self.
            default_notebook_metadata_filter)
    if self.default_cell_metadata_filter:
        format_options.setdefault('cell_metadata_filter', self.
            default_cell_metadata_filter)
    if self.comment_magics is not None:
        format_options.setdefault('comment_magics', self.comment_magics)
    if self.split_at_heading:
        format_options.setdefault('split_at_heading', self.split_at_heading)
    if not read and self.default_cell_markers:
        format_options.setdefault('cell_markers', self.default_cell_markers)
    if read and self.sphinx_convert_rst2md:
        format_options.setdefault('rst2md', self.sphinx_convert_rst2md)