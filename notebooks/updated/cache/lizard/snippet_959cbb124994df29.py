def load_from_docinfo(self, docinfo, delete_missing=False, raise_failure=False
    ):
    for uri, shortkey, docinfo_name, converter in self.DOCINFO_MAPPING:
        qname = QName(uri, shortkey)
        val = docinfo.get(str(docinfo_name))
        if val is None:
            if delete_missing and qname in self:
                del self[qname]
            continue
        try:
            val = str(val)
            if converter:
                val = converter.xmp_from_docinfo(val)
            if not val:
                continue
            self[qname] = val
        except (ValueError, AttributeError) as e:
            msg = 'The metadata field {} could not be copied to XMP'.format(
                docinfo_name)
            if raise_failure:
                raise ValueError(msg) from e
            else:
                warn(msg)