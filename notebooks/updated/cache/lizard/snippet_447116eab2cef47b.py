def expect(self, expect, searchwindowsize=None, maxread=None, timeout=None,
    iteration_n=1):
    if isinstance(expect, str):
        expect = [expect]
    if searchwindowsize != None:
        old_searchwindowsize = self.pexpect_child.searchwindowsize
        self.pexpect_child.searchwindowsize = searchwindowsize
    if maxread != None:
        old_maxread = self.pexpect_child.maxread
        self.pexpect_child.maxread = maxread
    res = self.pexpect_child.expect(expect + [pexpect.TIMEOUT] + [pexpect.
        EOF], timeout=timeout)
    if searchwindowsize != None:
        self.pexpect_child.searchwindowsize = old_searchwindowsize
    if maxread != None:
        self.pexpect_child.maxread = old_maxread
    if shutit_global.shutit_global_object.pane_manager and iteration_n == 1:
        time_seen = time.time()
        lines_to_add = []
        if isinstance(self.pexpect_child.before, (str, unicode)):
            for line_str in self.pexpect_child.before.split('\n'):
                lines_to_add.append(line_str)
        if isinstance(self.pexpect_child.after, (str, unicode)):
            for line_str in self.pexpect_child.after.split('\n'):
                lines_to_add.append(line_str)
        for line in lines_to_add:
            self.session_output_lines.append(SessionPaneLine(line_str=line,
                time_seen=time_seen, line_type='output'))
    return res