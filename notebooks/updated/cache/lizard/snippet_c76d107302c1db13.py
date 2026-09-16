def extract_content(self, selector='', attr='', default='', connector='', *
    args, **kwargs):
    try:
        if selector.lower() == 'url':
            return self.url
        if attr.lower() == 'text':
            tag = self.get_tree_tag(selector=selector, get_one=True)
            content = connector.join([make_ascii(x).strip() for x in tag.
                itertext()])
            content = content.replace('\n', ' ').strip()
        else:
            tag = self.get_tree_tag(selector=selector, get_one=True)
            content = tag.get(attr)
            if attr in ['href', 'src']:
                content = urljoin(self.url, content)
        return content
    except IndexError:
        if default is not '':
            return default
        raise Exception('There is no content for the %s selector - %s' % (
            self.__selector_type__, selector))
    except XPathError:
        raise Exception('Invalid %s selector - %s' % (self.
            __selector_type__, selector))