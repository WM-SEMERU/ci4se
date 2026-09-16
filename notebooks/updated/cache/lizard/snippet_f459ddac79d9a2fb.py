def should_break_here(self, frame):
    c_file_name = self.canonic(frame.f_code.co_filename)
    if not c_file_name in IKBreakpoint.breakpoints_files:
        return False
    bp = IKBreakpoint.lookup_effective_breakpoint(c_file_name, frame.
        f_lineno, frame)
    return True if bp else False