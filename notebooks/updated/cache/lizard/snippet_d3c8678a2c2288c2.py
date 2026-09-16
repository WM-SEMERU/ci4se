def init_read_line(self):
    format_list = self._format_list
    self._re_cvt = self.match_input_fmt(format_list)
    regexp0_str = ''.join([subs[0] for subs in self._re_cvt])
    self._regexp_str = regexp0_str
    self._re = re.compile(regexp0_str)
    self._match_exps = [subs[1] for subs in self._re_cvt if subs[1] is not None
        ]
    self._divisors = [subs[2] for subs in self._re_cvt if subs[2] is not None]
    self._in_cvt_fns = [subs[3] for subs in self._re_cvt if subs[3] is not None
        ]
    self._read_line_init = True