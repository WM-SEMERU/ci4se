def get_meta(self, key, conforming=True):
    try:
        metas = list(self.bucket.list(prefix=key))
        metas = wrap([m for m in metas if m.name.find('.json') != -1])
        perfect = Null
        favorite = Null
        too_many = False
        error = None
        for m in metas:
            try:
                simple = strip_extension(m.key)
                if conforming:
                    self._verify_key_format(simple)
                if simple == key:
                    perfect = m
                    too_many = False
                if simple.startswith(key + '.') or simple.startswith(key + ':'
                    ):
                    if favorite and not perfect:
                        too_many = True
                    favorite = m
            except Exception as e:
                error = e
        if too_many:
            Log.error(
                'multiple keys in {{bucket}} with prefix={{prefix|quote}}: {{list}}'
                , bucket=self.name, prefix=key, list=[k.name for k in metas])
        if not perfect and error:
            Log.error('Problem with key request', error)
        return coalesce(perfect, favorite)
    except Exception as e:
        Log.error(READ_ERROR + ' can not read {{key}} from {{bucket}}', key
            =key, bucket=self.bucket.name, cause=e)