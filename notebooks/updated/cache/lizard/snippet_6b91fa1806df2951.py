def str2dict(self, rawstr):
    kw_list = []
    sp1 = rawstr.split(':')
    kw_name = sp1[0].strip().upper()
    kw_desc = sp1[1:]
    sp2 = kw_desc[0].replace(',', ';;', 1).split(';;')
    kw_type = sp2[0].strip()
    try:
        kw_vals = sp2[1].replace(',', '=').split('=')
        [(not (i.isspace() or i == '') and kw_list.append(i)) for i in kw_vals]
        ks = [k.strip() for k in kw_list[0::2]]
        vs = [v.strip().replace('"', '').replace("'", '') for v in kw_list[
            1::2]]
        kw_vals_dict = dict(zip(ks, vs))
        rdict = {kw_name: {kw_type: kw_vals_dict}}
    except:
        rdict = {kw_name: kw_type}
    return rdict