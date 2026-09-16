def _cat_num_pt_xml(self):
    xml = ''
    for idx, category in enumerate(self._series.categories):
        xml += (
            """                <c:pt idx="{cat_idx}">
                  <c:v>{cat_lbl_str}</c:v>
                </c:pt>
"""
            .format(**{'cat_idx': idx, 'cat_lbl_str': category.
            numeric_str_val(self._date_1904)}))
    return xml