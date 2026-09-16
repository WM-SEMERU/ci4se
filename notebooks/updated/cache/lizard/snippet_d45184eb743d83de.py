def find_frame_urls(self, site, frametype, gpsstart, gpsend, match=None,
    urltype=None, on_gaps='warn'):
    if on_gaps not in ('warn', 'error', 'ignore'):
        raise ValueError("on_gaps must be 'warn', 'error', or 'ignore'.")
    url = '%s/gwf/%s/%s/%s,%s' % (_url_prefix, site, frametype, gpsstart,
        gpsend)
    if urltype:
        url += '/%s' % urltype
    url += '.json'
    if match:
        url += '?match=%s' % match
    response = self._requestresponse('GET', url)
    urllist = decode(response.read())
    out = lal.Cache([lal.CacheEntry.from_T050017(x, coltype=self.
        LIGOTimeGPSType) for x in urllist])
    if on_gaps == 'ignore':
        return out
    else:
        span = segments.segment(gpsstart, gpsend)
        seglist = segments.segmentlist(e.segment for e in out).coalesce()
        missing = (segments.segmentlist([span]) - seglist).coalesce()
        if span in seglist:
            return out
        else:
            msg = 'Missing segments: \n%s' % '\n'.join(map(str, missing))
            if on_gaps == 'warn':
                sys.stderr.write('%s\n' % msg)
                return out
            else:
                raise RuntimeError(msg)