def autodecode(self, a_bytes):
    try:
        analysis = chardet.detect(a_bytes)
        if analysis['confidence'] >= 0.75:
            return self.decode(a_bytes, analysis['encoding'])[0], analysis[
                'encoding']
        else:
            raise Exception('Failed to detect encoding. (%s, %s)' % (
                analysis['confidence'], analysis['encoding']))
    except NameError:
        print(
            'Warning! chardet not found. Use utf-8 as default encoding instead.'
            )
        return a_bytes.decode('utf-8')[0], 'utf-8'