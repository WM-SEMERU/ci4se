def _get_stack_info_for_trace(self, frames, library_frame_context_lines=
    None, in_app_frame_context_lines=None, with_locals=True,
    locals_processor_func=None):
    return list(iterate_with_template_sources(frames, with_locals=
        with_locals, library_frame_context_lines=
        library_frame_context_lines, in_app_frame_context_lines=
        in_app_frame_context_lines, include_paths_re=self.include_paths_re,
        exclude_paths_re=self.exclude_paths_re, locals_processor_func=
        locals_processor_func))