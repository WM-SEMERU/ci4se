def populate_hazard_classification(self):
    new_class = {'value': self.radius_form.value(), 'name': self.class_form
        .text()}
    self.classification.append(new_class)
    self.classification = sorted(self.classification, key=itemgetter('value'))
    self.hazard_class_form.clear()
    for item in self.classification:
        new_item = '{value} - {name}'.format(value=item['value'], name=item
            ['name'])
        self.hazard_class_form.addItem(new_item)
    self.radius_form.setValue(0)
    self.class_form.clear()
    self.ok_button_status()