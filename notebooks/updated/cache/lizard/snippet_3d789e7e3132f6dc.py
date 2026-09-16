def folderitem(self, obj, item, index):
    url = item.get('url')
    title = item.get('Title')
    calibrator = obj.getCalibrator()
    item['getDownFrom'] = self.localize_date(obj.getDownFrom())
    item['getDownTo'] = self.localize_date(obj.getDownTo())
    item['getCalibrator'] = ''
    if calibrator:
        props = api.get_user_properties(calibrator)
        name = props.get('fullname', calibrator)
        item['getCalibrator'] = name
    item['replace']['Title'] = get_link(url, value=title)
    if obj == self.latest_calibration:
        item['state_class'] = 'state-published'
    elif obj in self.active_calibrations:
        item['state_class'] = 'state-active'
    else:
        item['state_class'] = 'state-inactive'
    return item