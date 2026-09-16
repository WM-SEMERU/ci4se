def headercontent(self, method):
    content = []
    wsse = self.options().wsse
    if wsse is not None:
        content.append(wsse.xml())
    headers = self.options().soapheaders
    if not isinstance(headers, (tuple, list, dict)):
        headers = headers,
    elif not headers:
        return content
    pts = self.headpart_types(method)
    if isinstance(headers, (tuple, list)):
        n = 0
        for header in headers:
            if isinstance(header, Element):
                content.append(deepcopy(header))
                continue
            if len(pts) == n:
                break
            h = self.mkheader(method, pts[n], header)
            ns = pts[n][1].namespace('ns0')
            h.setPrefix(ns[0], ns[1])
            content.append(h)
            n += 1
    else:
        for pt in pts:
            header = headers.get(pt[0])
            if header is None:
                continue
            h = self.mkheader(method, pt, header)
            ns = pt[1].namespace('ns0')
            h.setPrefix(ns[0], ns[1])
            content.append(h)
    return content