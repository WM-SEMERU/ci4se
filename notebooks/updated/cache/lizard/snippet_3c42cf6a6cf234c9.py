def toc_html(self, depth=6, lowest_level=6):
    toc = self.toc(depth=depth, lowest_level=lowest_level)
    if not toc:
        return ''

    def map_toc_list(toc_list):
        result = ''
        if toc_list:
            result += '<ul>\n'
            result += ''.join(map(lambda x:
                '<li><a href="#{}">{}</a>{}</li>\n'.format(x['id'], x[
                'inner_html'], map_toc_list(x['children'])), toc_list))
            result += '</ul>'
        return result
    return map_toc_list(toc)