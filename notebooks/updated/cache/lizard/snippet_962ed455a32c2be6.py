def get_nts_flat(self, hdrgo_prt=True, use_sections=True):
    if self.sectobj is None or not use_sections:
        return self.sortgos.get_nts_sorted(hdrgo_prt, hdrgos=self.grprobj.
            get_hdrgos(), hdrgo_sort=True)
    if not use_sections:
        return self.sectobj.get_sorted_nts_omit_section(hdrgo_prt,
            hdrgo_sort=True)
    return None