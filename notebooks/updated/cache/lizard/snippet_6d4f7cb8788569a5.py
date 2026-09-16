def set_widgets(self):
    source = self.parent.get_existing_keyword('source')
    if source or source == 0:
        self.leSource.setText(source)
    else:
        self.leSource.clear()
    source_scale = self.parent.get_existing_keyword('scale')
    if source_scale or source_scale == 0:
        self.leSource_scale.setText(source_scale)
    else:
        self.leSource_scale.clear()
    source_date = self.parent.get_existing_keyword('date')
    if source_date:
        self.ckbSource_date.setChecked(True)
        self.dtSource_date.setDateTime(source_date)
    else:
        self.ckbSource_date.setChecked(False)
        self.dtSource_date.clear()
    source_url = self.parent.get_existing_keyword('url')
    try:
        source_url = source_url.toString()
    except AttributeError:
        pass
    if source_url or source_url == 0:
        self.leSource_url.setText(source_url)
    else:
        self.leSource_url.clear()
    source_license = self.parent.get_existing_keyword('license')
    if source_license or source_license == 0:
        self.leSource_license.setText(source_license)
    else:
        self.leSource_license.clear()