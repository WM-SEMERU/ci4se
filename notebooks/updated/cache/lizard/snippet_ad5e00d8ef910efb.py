def filterItems(self, terms, autoExpand=True, caseSensitive=False):
    if type(terms) != dict:
        terms = {'*': nativestring(terms)}
    if type(terms) != dict:
        terms = {'*': nativestring(terms)}
    if '*' in terms and type(terms['*']) != list:
        sterms = nativestring(terms['*'])
        if not sterms.strip():
            terms.pop('*')
        else:
            dtype_matches = COLUMN_FILTER_EXPR.findall(sterms)
            for match, dtype, values in dtype_matches:
                sterms = sterms.replace(match, '')
                terms.setdefault(dtype, [])
                terms[dtype] += values.split(',')
            keywords = sterms.replace(',', '').split()
            while '' in keywords:
                keywords.remove('')
            terms['*'] = keywords
    filtered_columns = self.filteredColumns()
    filter_terms = {}
    for column, keywords in terms.items():
        index = self.column(column)
        if column != '*' and not index in filtered_columns:
            continue
        if not caseSensitive:
            keywords = [nativestring(keyword).lower() for keyword in keywords]
        else:
            keywords = map(str, keywords)
        filter_terms[index] = keywords
    self.__filterItems(filter_terms, autoExpand, caseSensitive, 0)