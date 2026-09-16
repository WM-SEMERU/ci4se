def _wrlog_details_illegal_gaf(self, fout_err, err_cnts):
    gaf_base = os.path.basename(fout_err)
    with open(fout_err, 'w') as prt:
        prt.write('ILLEGAL GAF ERROR SUMMARY:\n\n')
        for err_cnt in err_cnts:
            prt.write(err_cnt)
        prt.write('\n\nILLEGAL GAF ERROR DETAILS:\n\n')
        for lnum, line in self.ignored:
            prt.write('**WARNING: GAF LINE IGNORED: {FIN}[{LNUM}]:\n{L}\n'.
                format(FIN=gaf_base, L=line, LNUM=lnum))
            self.prt_line_detail(prt, line)
            prt.write('\n\n')
        for error, lines in self.illegal_lines.items():
            for lnum, line in lines:
                prt.write(
                    '**WARNING: GAF LINE ILLEGAL({ERR}): {FIN}[{LNUM}]:\n{L}\n'
                    .format(ERR=error, FIN=gaf_base, L=line, LNUM=lnum))
                self.prt_line_detail(prt, line)
                prt.write('\n\n')
    return fout_err