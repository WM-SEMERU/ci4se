def _postprocess(self):
    self._POST['P0601010__a'] = self._validate_isbn(self._POST[
        'P0601010__a'], accept_blank=True)
    if self._POST['P0601010__a'] != '':
        self._POST['P0601010__b'] = 'soubor : ' + self._POST['P0601010__a']
    self._POST['P0501010__a'] = self._validate_isbn(self._POST[
        'P0501010__a'], accept_blank=False)
    self._POST['P1601ISB__a'] = self._POST['P0501010__a']