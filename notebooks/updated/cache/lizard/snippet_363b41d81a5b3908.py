def get_sections_2d(self):
    sections_hdrgos_act = []
    hdrgos_act_all = self.get_hdrgos()
    hdrgos_act_secs = set()
    if self.hdrobj.sections:
        for section_name, hdrgos_all_lst in self.hdrobj.sections:
            hdrgos_all_set = set(hdrgos_all_lst)
            hdrgos_act_set = hdrgos_all_set.intersection(hdrgos_act_all)
            if hdrgos_act_set:
                hdrgos_act_secs |= hdrgos_act_set
                hdrgos_act_lst = []
                hdrgos_act_ctr = cx.Counter()
                for hdrgo_p in hdrgos_all_lst:
                    if hdrgo_p in hdrgos_act_set and hdrgos_act_ctr[hdrgo_p
                        ] == 0:
                        hdrgos_act_lst.append(hdrgo_p)
                    hdrgos_act_ctr[hdrgo_p] += 1
                sections_hdrgos_act.append((section_name, hdrgos_act_lst))
        hdrgos_act_rem = hdrgos_act_all.difference(hdrgos_act_secs)
        if hdrgos_act_rem:
            sections_hdrgos_act.append((self.hdrobj.secdflt, hdrgos_act_rem))
    else:
        sections_hdrgos_act.append((self.hdrobj.secdflt, hdrgos_act_all))
    return sections_hdrgos_act