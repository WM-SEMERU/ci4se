def __output_unpaired_vals(d_vals, used_ff_keys, f_f_header, sf_d,
    s_f_header, missing_val, out_handler, outfh, delim='\t'):
    if missing_val is None:
        raise MissingValueError('Need missing value to output ' +
            ' unpaired lines')
    for k in d_vals:
        if k not in used_ff_keys:
            f_f_flds = d_vals[k]
            if s_f_header is not None:
                s_f_flds = [dict(zip(s_f_header, [missing_val] * len(
                    s_f_header)))]
            else:
                s_f_num_cols = len(sf_d[d_vals.keys()[0]][0])
                s_f_flds = [[missing_val] * s_f_num_cols]
            out_handler.write_output(outfh, delim, s_f_flds, f_f_flds,
                s_f_header, f_f_header)