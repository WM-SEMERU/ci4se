def _parse_tmx(path):

    def _get_tuv_lang(tuv):
        for k, v in tuv.items():
            if k.endswith('}lang'):
                return v
        raise AssertionError('Language not found in `tuv` attributes.')

    def _get_tuv_seg(tuv):
        segs = tuv.findall('seg')
        assert len(segs) == 1, 'Invalid number of segments: %d' % len(segs)
        return segs[0].text
    with tf.io.gfile.GFile(path) as f:
        for _, elem in ElementTree.iterparse(f):
            if elem.tag == 'tu':
                yield {_get_tuv_lang(tuv): _get_tuv_seg(tuv) for tuv in
                    elem.iterfind('tuv')}
                elem.clear()